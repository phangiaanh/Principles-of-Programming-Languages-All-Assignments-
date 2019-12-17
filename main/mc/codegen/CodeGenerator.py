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
    def printCode(self, code, o, typ):
        if isinstance(o, SubBody):
            return self.emit.printout(code)
        elif isinstance(o, Access):
            return code, typ


    def genMETHOD(self, consdecl, sym, frame):
        #consdecl: FuncDecl
        #sym: Any
        #frame: Frame

        #1. Setup declarations
        #Check if it is init, clinit, main or regular functions
        isInit = (consdecl.name.name == "<init>")
        isClInit = (consdecl.name.name == "<clinit>")
        # isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and isinstance(consdecl.returnType, VoidType)
        isMain = consdecl.name.name == "main"

        #Get return type
        returnType = VoidType() if (isInit or isClInit) else consdecl.returnType
        
        #Get method name
        methodName = consdecl.name.name
        
        #Get inType
        intype = None
        if isMain:
            intype = [ArrayPointerType(StringType())]
        elif isInit or isClInit:
            intype = []
        else:
            intype = [x.varType for x in consdecl.param] 

        #Get MType
        mtype = MType(intype, returnType)

        #2. Create 
        # import pdb
        # pdb.set_trace()
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        #3. Enter Scope
        frame.enterScope(True)

        #4. Generate code for declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        e = SubBody(frame, sym)
        if not isInit and not isClInit:
            for x in consdecl.param:
                e = self.visit(x, e)
            for x in consdecl.body.member:
                if isinstance(x, VarDecl):
                    e = self.visit(x, e)

        globalEnvi = e.sym
        frame = e.frame
        body = consdecl.body

        #Start of body: Create new label
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if isMain:
            #Generate code for local variables only
            for x in globalEnvi:
                VarDeclJasminArray = None
                if isinstance(x.mtype, ArrayType) and x.value is not None:
                    if isinstance(x.mtype.eleType, StringType):
                        VarDeclJasminArray = self.emit.emitANEWARRAY(x.name, x.mtype, x.value, frame)
                    else:
                        VarDeclJasminArray = self.emit.emitNEWARRAY(x.name, x.mtype, x.value, frame)
                    self.emit.printout(VarDeclJasminArray)

        #Normal function
        if not isMain and not isInit and not isClInit:
            for x in body.member:
                if isinstance(x, VarDecl) and isinstance(x.mtype, ArrayType):
                    VarDeclJasminArray = None
                    varFound = self.lookup(x.variable, globalEnvi[::-1], lambda y: y.name)
                    if varFound.value is not None:
                        if isinstance(varFound.mtype.eleType, StringType):
                            VarDeclJasminArray = self.emit.emitANEWARRAY(VarFound.name, VarFound.mtype, VarFound.value, frame)
                        else:
                            VarDeclJasminArray = self.emit.emitNEWARRAY(VarFound.name, VarFound.mtype, VarFound.value, frame)
                        self.emit.printout(VarDeclJasminArray)

        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        if isClInit:
            for x in globalEnvi:
                VarDeclJasminArray = None
                if isinstance(x.mtype, ArrayType) and x.value is None:
                    if isinstance(x.mtype.eleType, StringType):
                        VarDeclJasminArray = self.emit.emitANEWARRAY(self.className + "." + x.name, x.mtype, x.value, frame)
                    else:
                        VarDeclJasminArray = self.emit.emitNEWARRAY(self.className + "." + x.name, x.mtype, x.value, frame)
                    self.emit.printout(VarDeclJasminArray)
        


        #5. Generate code for statements
        for x in body.member:
            if not isinstance(x, VarDecl):
                self.visit(x, SubBody(frame, globalEnvi))
        # list(map(lambda x: self.visit(x, SubBody(frame, globalEnvi)), body.member))

        #6. Finish labels
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(returnType, frame))
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
        e = SubBody(Frame(None, None), self.env)
        
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
        for x in FuncList:
            sym = e.sym

            #Set frame properties as the current function
            frame.name = x.name.name
            frame.returnType = x.returnType
            
            #Generate code for every function
            self.genMETHOD(x, sym, frame)

        #4. Generate constructor for class
        self.genMETHOD(FuncDecl(Id("<init>"), [], None, Block([])), e.sym, Frame("<init>", VoidType))

        #5. Create clinit for array constructor
        for x in e.sym:
            #If x is a Symbol of a variable which type is ArrayType
            if isinstance(x.mtype, ArrayType):
                self.genMETHOD(FuncDecl(Id("<clinit>"), [], None, Block([])), e.sym, Frame("<clinit>", VoidType))
                #ArrayType constructor only need to be called once
                break

        #6. Write to file .j
        self.emit.emitEPILOG()
        return c


    def visitVarDecl(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym

        #Check if the VarDecl is global or local
        #If the indexLocal field is empty(there is no new scope), set isGlobal
        isGlobal = (len(frame.indexLocal) == 0)
        VarDeclJasmin = None
        
        if isGlobal:
            #Call emitATTRIBUTE for static variable(global)
            VarDeclJasmin = self.emit.emitATTRIBUTE(ast.variable, ast.varType, False, None)
            sym.append(Symbol(ast.variable, ast.varType, None))
        else:
            #New index for a new variable
            idx = frame.getNewIndex()
            #Call emitVAR for variable in scope
            VarDeclJasmin = self.emit.emitVAR(idx, ast.variable, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame) 
            sym.append(Symbol(ast.variable, ast.varType, idx))
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

        #Return new SubBody with a new Symbol
        return SubBody(frame, sym + [Symbol(ast.name.name, MType(list(map(lambda x: x.varType, ast.param)), ast.returnType), CName(self.className))])


    def visitBinaryOp(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        #Check if the operator is "="
        if ast.op != "=":
            #Visit left and rignt first, then the operator
            leftString, leftType = self.visit(ast.left, Access(frame, nenv, False, False))
            rightString, rightType = self.visit(ast.right, Access(frame, nenv, False, False))
            
            #Boolean Operators
            if isinstance(leftType, BoolType) or isinstance(rightType, BoolType):
                if ast.op == "&&":
                    return self.printCode(leftString + rightString + self.emit.emitANDOP(frame), ctxt, BoolType())
                elif ast.op == "||":
                    return self.printCode(leftString + rightString + self.emit.emitOROP(frame), ctxt, BoolType())
                elif ast.op in ["==", "!="]:
                    return self.printCode(leftString + rightString + self.emit.emitREOP(ast.op, BoolType(), frame), ctxt, BoolType())
            
            #Integer Operators
            if isinstance(leftType, IntType) and isinstance(rightType, IntType):
                if ast.op in ["+", "-"]:
                    return self.printCode(leftString + rightString + self.emit.emitADDOP(ast.op, IntType(), frame), ctxt, IntType())
                elif ast.op == "*":
                    return self.printCode(leftString + rightString + self.emit.emitMULOP(ast.op, IntType(), frame), ctxt, IntType())
                elif ast.op == "/":
                    return self.printCode(leftString + rightString + self.emit.emitDIV(frame), ctxt, IntType())
                elif ast.op == "%":
                    return self.printCode(leftString + rightString + self.emit.emitMOD(frame), ctxt, IntType())
                elif ast.op in [">", ">=", "<", "<=", "==", "!="]:
                    return self.printCode(leftString + rightString + self.emit.emitREOP(ast.op, IntType(), frame), ctxt, BoolType())

            #Convert to Floating 
            if isinstance(leftType, IntType):
                leftString = leftString + self.emit.emitI2F(frame)
            if isinstance(rightType, IntType):
                rightString = rightString + self.emit.emitI2F(frame)

            #Floating Operators
            if ast.op in ["+", "-"]:
                return self.printCode(leftString + rightString + self.emit.emitADDOP(ast.op, FloatType(), frame), ctxt, FloatType())
            elif ast.op in ["*", "/"]:
                return self.printCode(leftString + rightString + self.emit.emitMULOP(ast.op, FloatType(), frame), ctxt, FloatType())
            elif ast.op in ["<", "<=", ">", ">="]:
                return self.printCode(leftString + rightString + self.emit.emitFREOP(ast.op, FloatType(), frame), ctxt, FloatType())
        
        else:

            leftString, leftType = self.visit(ast.left,Access(frame,nenv,True,True))
            rightString, rightType = self.visit(ast.right,Access(frame,nenv,False,False)) 
            leftStringExtra, _ = self.visit(ast.left,Access(frame,nenv,True,False))

            coercion = isinstance(rightType, IntType) and isinstance(leftType, FloatType)

            finalCode = leftString + rightString + (self.emit.emitI2F(frame) if coercion else "") + leftStringExtra
            return self.printCode(finalCode, ctxt, leftType)


    def visitUnaryOp(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        unaString, unaType = self.visit(ast.body, Access(frame, nenv, False, False))

        if ast.op != "!":
            return self.printCode(unaString + self.emit.emitNEGOP(unaType, frame), ctxt, unaType)
        else:
            return self.printCode(unaString + self.emit.emitNOT(unaType, frame), ctxt, unaType)


    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        #Get function symbol
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        
        #Get function class name and type
        cname = sym.value.value
        ctype = sym.mtype

        in_ = ""
        i = 0
        
        for x in ast.param:
            str1,typ1 = self.visit(x, Access(frame, nenv, False, False))
            in_ += str1
            if isinstance(sym.mtype.partype[i], FloatType) and isinstance(typ1, IntType):
                in_ += self.emit.emitI2F(frame)
            i += 1   

        #Concatenate two strings
        finalCode = in_ + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame)
        return self.printCode(finalCode, ctxt, sym.mtype.rettype)


    def visitId(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        #ctxt must be Access
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst

        id = self.lookup(ast.name, nenv[::-1], lambda x: x.name)

        #LHS visit the first time
        if isLeft and isFirst:
            #If not ArrayType, doing nothing because this is the first time visit
            if not isinstance(id.mtype, ArrayType):
                return self.printCode("", ctxt, id.mtype)
            else:
                #If local, emit READVAR. If global, emit GETSTATIC
                if id.value is not None:
                    return self.printCode(self.emit.emitREADVAR(id.name, id.mtype, id.value, frame), ctxt, id.mtype)
                else:
                    return self.printCode(self.emit.emitGETSTATIC(self.className + "." + id.name, id.mtype, frame), ctxt, id.mtype)

        #RHS
        if not isLeft and not isFirst:
            if id.value is not None:
                return self.printCode(self.emit.emitREADVAR(id.name, id.mtype, id.value, frame), ctxt, id.mtype)
            else:
                return self.printCode(self.emit.emitGETSTATIC(self.className + "." + id.name, id.mtype, frame), ctxt, id.mtype)
        
        #LHS visit the second time
        if isLeft and not isFirst:
            if not isinstance(id.mtype, ArrayType):
                if id.value is None:
                    return self.printCode(self.emit.emitPUTSTATIC(self.className + "." + id.name, id.mtype, frame), ctxt, id.mtype)
                else:
                    return self.printCode(self.emit.emitWRITEVAR(id.name, id.mtype, id.value, frame), ctxt, id.mtype)
            else:
                return self.printCode(self.emit.emitASTORE(id.mtype.eleType, frame), ctxt, id.mtype.eleType)


    def visitArrayCell(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        #ctxt must be Access
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst

        #LHS visit the first time
        if isLeft and isFirst:
            arrString, arrType = self.visit(ast.arr, Access(frame, nenv, True, True))
            idxString, idxType = self.visit(ast.idx, Access(frame, nenv, False, False))

            arrString += idxString
            return self.printCode(arrString, ctxt, arrType.eleType)

        if not isLeft and not isFirst:
            arrString, arrType = self.visit(ast.arr, Access(frame, nenv, True, True))
            idxString, idxType = self.visit(ast.idx, Access(frame, nenv, False, False))

            arrString += idxString
            arrString += self.emit.emitALOAD(arrType.eleType, frame)
            return self.printCode(arrString, ctxt, arrType.eleType)

        if isLeft and not isFirst:
            return self.visit(ast.arr, Access(frame, nenv, True, False))


    def visitIf(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        thenStmt = ast.thenStmt
        elseStmt = ast.elseStmt

        #Code for expr
        exprString, exprType = self.visit(ast.expr, Access(frame, nenv, False, False))
        self.emit.printout(exprString)

        #Create two new labels
        trueLabel = frame.getNewLabel()
        falseLabel = frame.getNewLabel()

        #Code IFTRUE + trueLabel
        self.emit.printout(self.emit.emitIFTRUE(trueLabel, frame))

        #Check elseStmt
        if elseStmt is not None:
            elseSubBody = SubBody(frame, nenv)
            self.visit(elseStmt, elseSubBody)
        
        #Labels
        self.emit.printout(self.emit.emitGOTO(falseLabel,frame))
        self.emit.printout(self.emit.emitLABEL(trueLabel,frame))
        thenSubBody = SubBody(frame, nenv)
        self.visit(thenStmt, thenSubBody)

        #Out
        self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
        


    def visitReturn(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        if ast.expr is not None:
            exprString, exprType = self.visit(ast.expr, Access(frame, nenv, False, False))
            self.emit.printout(exprString)

            if isinstance(exprType, IntType) and isinstance(frame.returnType, FloatType):
                self.emit.printout(self.emit.emitI2F(frame))

        self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))



    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()
    

    def visitFloatLiteral(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(ast.value, frame), FloatType()


    def visitBooleanLiteral(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value), frame),  BoolType()


    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST('"' + ast.value + '"', StringType(), frame), StringType()
    #===============================================

#=========================================================================
    
