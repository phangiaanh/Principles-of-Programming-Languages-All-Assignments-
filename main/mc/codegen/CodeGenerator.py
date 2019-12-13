'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod


#==============================SUPPORTING CLASSES==============================
class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value
#==============================================================================


#==============================CODE GENERATOR==============================
class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return  [
                Symbol("getInt",MType([],IntType()), CName(self.libName)),
                Symbol("putInt",MType([IntType()],VoidType()), CName(self.libName)),
                Symbol("putIntLn",MType([IntType()],VoidType()), CName(self.libName)),
                Symbol("getFloat",MType([],FloatType()), CName(self.libName)),
                Symbol("putFloat",MType([FloatType()],VoidType()), CName(self.libName)),
                Symbol("putFloatLn",MType([FloatType()],VoidType()), CName(self.libName)),
                Symbol("putBool",MType([BoolType()],VoidType()), CName(self.libName)),
                Symbol("putBoolLn",MType([BoolType()],VoidType()), CName(self.libName)),
                Symbol("putString",MType([StringType()],VoidType()), CName(self.libName)),
                Symbol("putStringLn",MType([StringType()],VoidType()), CName(self.libName)),
                Symbol("putLn",MType([],VoidType()), CName(self.libName))
                ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)
#==========================================================================


#==============================CODE VISITTOR==============================
class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    #====================METHOD GENERATOR====================
    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else []
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.member))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
    #========================================================



    #====================VISITOR====================
    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        #1. Set parent class
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        #2. Create SubBody
        e = SubBody(None, self.env)
        
        #3.1. Visit VarDecl
        FuncList = []
        for x in ast.decl:
            if isinstance(x, VarDecl):
                e = self.visit(x, e)
            else:
                FuncList.append(x)
        
        #3.2.1. Visit FuncDecl first time
        for x in FuncList:
            e = self.visit(x, e)

        #3.2.2. Visit FuncDecl second time
        frame = e.frame

        
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), [], None, Block([])), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c


    def visitVarDecl(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym

        #Check if the VarDecl is global or local
        #If the indexLocal field is empty(there is no new scope), set isGlobal
        isGlobal = (len(frame.indecLocal) == 0)
        VarDeclJasmin = None
        
        if isGlobal:
            #Call emitATTRIBUTE for static variable(global)
            VarDeclJasmin = self.emit.emitATTRIBUTE(ast.variable.name, ast.varType, False, None)
            sym.append(Symbol(ast.variable.name, ast.varType, None))
        else:
            #Call emitVAR for variable in scope
            idx = frame.getNewIndex()
            VarDeclJasmin = self.emit.emitVAR(idx, ast.variable.name, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame) 
            sym.append(Symbol(ast.variable.name, ast.varType, idx))
        self.emit.printout(VarDeclJasmin)
        return SubBody(frame, sym)


    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        
        #Check the frame
        if frame is None:
            frame = Frame(ast.name.name, ast.returnType)
        else:
            #frame holds the current function's properties 
            frame.name = ast.name.name
            frame.returnType = ast.returnType

        return SubBody(frame, sym + [Symbol(ast.name.name, MType(list(map(lambda x: x.varType, ast.param)), ast.returnType),)])

    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", [])
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()
    
    #===============================================

#=========================================================================
    
