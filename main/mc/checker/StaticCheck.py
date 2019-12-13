# ID: 1710009
# Name: Phan Gia Anh
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import *
import operator

ope = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv, "//":operator.floordiv, "%":operator.mod, "<":operator.lt, "<=":operator.le, ">":operator.gt, ">=":operator.ge, "==":operator.eq, "!=":operator.ne, "&&":operator.and_, "||":operator.or_}

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):
    
    global_envi = [
        Symbol("getInt",MType([],IntType()), 1),
        Symbol("putInt",MType([IntType()],VoidType()), 1),
        Symbol("putIntLn",MType([IntType()],VoidType()), 1),
        Symbol("getFloat",MType([],FloatType()), 1),
        Symbol("putFloat",MType([FloatType()],VoidType()), 1),
        Symbol("putFloatLn",MType([FloatType()],VoidType()), 1),
        Symbol("putBool",MType([BoolType()],VoidType()), 1),
        Symbol("putBoolLn",MType([BoolType()],VoidType()), 1),
        Symbol("putString",MType([StringType()],VoidType()), 1),
        Symbol("putStringLn",MType([StringType()],VoidType()), 1),
        Symbol("putLn",MType([],VoidType()), 1)
    ]

    envi = [[]] 
    
    def __init__(self,ast):
        self.ast = ast

    def checkUnreach(self, ast, c):
        ref = c[-1][0][2][-1]
        if ref == [True, None] or ref == [True, True] or ref == True:
            raise UnreachableStatement(ast)
        if c[-1][-1] is not None:
            if c[-1][-1][-1] == [True, None] or c[-1][-1][-1] == [True, True] or c[-1][-1][-1] == True:
                raise UnreachableStatement(ast)  
 
    def check(self):
        StaticChecker.envi = [StaticChecker.global_envi]
        return self.visit(self.ast, StaticChecker.envi)

    def visitProgram(self, ast, c): 
        ref = (reduce(lambda x, y: x + self.visit(y, x) if isinstance(y, FuncDecl) else x + [self.visit(y, x[1:])], ast.decl,[-1] + c[-1]))[1:]
        for x in ref:
            if x.value is None:
                x.value = 0
        c.extend([ref])
        c.pop(0)
        if self.lookup(True, c[-1], lambda x: x.name == "main" and isinstance(x.mtype, MType)) is None:
            raise NoEntryPoint()
        [self.visit(x, c) for x in filter(lambda x: isinstance(x, FuncDecl), ast.decl)]
        ref = self.lookup(True, c[-1], lambda x: (x.name != "main") and isinstance(x.mtype, MType) and x.value == 0)
        if ref is not None:
            raise UnreachableFunction(ref.name)
        return None

    def visitFuncDecl(self,ast, c):
        if(c[0] == -1):
            if not c[1:] or (self.lookup(ast.name.name, c[1:], lambda x: x.name) is None):
                return [Symbol(ast.name.name, MType(list(map(lambda x: x.varType, ast.param)), ast.returnType), None)]
            raise Redeclared(Function(), ast.name.name)
        else:
            c.insert(0,[])
            c.extend([[[ast.returnType, ast.name.name, [False]]]])
            try:
                ref = reduce(lambda x, y: x + [self.visit(y, x)], ast.param, [])
            except Redeclared as e:
                raise Redeclared(Parameter(), e.n)
            for x in ref:
                x.value = 0
            c[0].extend(ref)
            for x in ast.body.member:
                if isinstance(x, VarDecl):
                    c[0].insert(0, self.visit(x, c[0]))
                else:
                    if isinstance(x, Id):
                        try:
                            self.visit(x, c)
                        except (TypeMismatchInExpression, UninitializedVariable) as e:
                            pass
                    else:
                        self.visit(x, c)
            ref = c[-1][0][2][0]
            if ref == False and not isinstance(ast.returnType, VoidType):
                raise FunctionNotReturn(ast.name.name)
            c.pop(0)
            c.pop()
            return None
    
    def visitVarDecl(self,ast,c):
        if not c or self.lookup(ast.variable, c, lambda x: x.name) is None:
            return Symbol(ast.variable, ast.varType)
        raise Redeclared(Variable(), ast.variable)

    def visitCallExpr(self, ast, c): 
        self.checkUnreach(ast, c)
        ref = self.lookup(ast.method.name, reduce(lambda x,y: x + y, c[1:-1], c[0]), lambda x: x.name)
        if not ref:
            raise Undeclared(Function(), ast.method.name)
        elif not isinstance(ref.mtype, MType):
            raise TypeMismatchInExpression(ast)
        elif len(ref.mtype.partype) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        else:
            if ast.method.name != c[-1][0][1]:
                index = c[-2].index(ref)
                ref.value = 1
                c[-2][index] = ref
            par = list(map(lambda x: self.visit(x, c), ast.param))
            ide = ref.mtype.partype
            reff = zip(ide, par)
            reff = reduce(lambda x, y: x + [[y[0],y[1]]], reff, [])
            for x in reff:
                if isinstance(x[1], IntLiteral):
                    x[1] = IntType()
                elif isinstance(x[1], FloatLiteral):
                    x[1] = FloatType()
                elif isinstance(x[1], StringLiteral):
                    x[1] = StringType()
                elif isinstance(x[1], BooleanLiteral):
                    x[1] = BoolType()
                if type(x[1]) != type(x[0]):
                    if not (isinstance(x[1], IntType) and isinstance(x[0], FloatType)) and not ((isinstance(x[1], ArrayType) and isinstance(x[0], ArrayPointerType) and type(x[1].eleType) == type(x[0].eleType))):
                        raise TypeMismatchInExpression(ast)
                if type(x[1]) == ArrayPointerType and type(x[1].eleType) != type(x[0].eleType):
                    raise TypeMismatchInExpression(ast)               
        return ref.mtype.rettype

    def visitId(self, ast, c):
        self.checkUnreach(ast, c)
        ref = self.lookup(True, reduce(lambda x,y: x + y, c[1:-1], c[0]), lambda k: (k.name == ast.name))
        if (not ref):
            raise Undeclared(Identifier(), ast.name)
        elif isinstance(ref.mtype, MType):
            raise TypeMismatchInExpression(ast)
        elif ref.value is None and not isinstance(ref.mtype, (ArrayType, ArrayPointerType)):
            raise UninitializedVariable(ref.name)
        return ref.mtype

    def visitDowhile(self, ast, c):
        self.checkUnreach(ast, c)
        if not isinstance(self.visit(ast.exp, c), (BoolType, BooleanLiteral)):
            raise TypeMismatchInStatement(ast)
        c[-1].extend([[False]])
        [self.visit(x, c) for x in ast.sl]
        c[-1].pop()

    def visitReturn(self, ast, c):
        self.checkUnreach(ast, c)
        if ast.expr is None:
            if not isinstance(c[-1][0][0], VoidType):
                raise TypeMismatchInStatement(ast)
        else:
            ref = self.visit(ast.expr, c)
            if isinstance(ref, IntLiteral):
                ref = IntType()
            elif isinstance(ref, FloatLiteral):
                ref = FloatType()
            elif isinstance(ref, StringLiteral):
                ref = StringType()
            elif isinstance(ref, BooleanLiteral):
                ref = BoolType()

            if type(ref) != type(c[-1][0][0]):
                if not (isinstance(ref, IntType) and isinstance(c[-1][0][0], FloatType)) and not (isinstance(ref, ArrayType) and isinstance(c[-1][0][0], ArrayPointerType) and type(ref.eleType) == type(c[-1][0][0].eleType)):
                    raise TypeMismatchInStatement(ast)
            if type(ref) == ArrayPointerType and type(ref.eleType) != type(c[-1][0][0].eleType):
                raise TypeMismatchInStatement(ast) 
        
        ref = c[-1][0][2][-1]
        if not isinstance(ref, list):
            c[-1][0][2][-1] = True
        else:
            if c[-1][0][2][-1][1] is None:
                c[-1][0][2][-1][0] = True
            else:
                c[-1][0][2][-1][1] = True
        return None
    
    def visitContinue(self, ast, c):
        self.checkUnreach(ast, c)
        if len(c[-1]) == 1:
            raise ContinueNotInLoop
        ref = c[-1][-1][-1]
        if not isinstance(ref, list):
            c[-1][-1][-1] = True
        else:
            if c[-1][-1][-1][1] is None:
                c[-1][-1][-1][0] = True
            else:
                c[-1][-1][-1][1] = True
    
    def visitBreak(self, ast, c):
        self.checkUnreach(ast, c)
        if len(c[-1]) == 1:
            raise BreakNotInLoop
        ref = c[-1][-1][-1]
        if not isinstance(ref, list):
            c[-1][-1][-1] = True
        else:
            if c[-1][-1][-1][1] is None:
                c[-1][-1][-1][0] = True
            else:
                c[-1][-1][-1][1] = True

    def visitFor(self, ast, c):
        self.checkUnreach(ast, c)
        if not isinstance(self.visit(ast.expr1, c), (IntType, IntLiteral)) or not isinstance(self.visit(ast.expr2, c), (BoolType, BooleanLiteral)) or not isinstance(self.visit(ast.expr3, c), (IntType, IntLiteral)):
            raise TypeMismatchInStatement(ast)
        ref = c[-1][0][2][-1]
        if isinstance(ref, list):
            c[-1][0][2].extend([[False, None]])
        else:
            c[-1][0][2][-1] = [False, None]
        c[-1].extend([[False]])
        self.visit(ast.loop, c)
        c[-1].pop()
        c[-1][0][2].pop()
        if not c[-1][0][2]:
            c[-1][0][2].extend([False])
        else:
            if c[-1][0][2][-1][1] is None:
                c[-1][0][2][-1][0] = False
            else:
                c[-1][0][2][-1][1] = False
        return None        

    def visitIf(self, ast, c):
        self.checkUnreach(ast, c)
        ref = c[-1][0][2][-1]
        if isinstance(ref, list):
            c[-1][0][2].extend([[False, None]])
        else:
            c[-1][0][2][-1] = [False, None]
        if len(c[-1]) > 1:
            if isinstance(c[-1][-1][-1], list):
                c[-1][-1].extend([[False, None]])
            else:
                c[-1][-1][-1] = [False, None]
        ref = self.visit(ast.expr, c)
        if not isinstance(ref, (BoolType, BooleanLiteral)):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, c)
        c[-1][0][2][-1][1] = False
        if len(c[-1]) > 1:
            c[-1][-1][-1][1] = False 
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, c)
        ref = c[-1][0][2].pop()
        ref = ref[0] and ref[1]
        if not c[-1][0][2]:
            c[-1][0][2].extend([ref])
        else:
            if c[-1][0][2][-1][1] is None:
                c[-1][0][2][-1][0] = ref
            else:
                c[-1][0][2][-1][1] = ref
        if len(c[-1]) > 1:
            ref = c[-1][-1].pop()
            ref = ref[0] and ref[1]
            if not c[-1][-1]:
                c[-1][-1].extend([ref])
            else:
                if c[-1][-1][-1][1] is None:
                    c[-1][-1][-1][0] = ref
                else:
                    c[-1][-1][-1][1] = ref
        return None
    
    def visitBlock(self, ast, c):
        self.checkUnreach(ast, c)
        c.insert(0,[])
        for x in ast.member:
            if isinstance(x, VarDecl):
                c[0].insert(0, self.visit(x, c[0]))
            else:
                if isinstance(x, Id):
                    try:
                        self.visit(x, c)
                    except (TypeMismatchInExpression, UninitializedVariable) as e:
                        pass
                else:
                    self.visit(x, c)
        c.pop(0)
        return None
    
    def visitUnaryOp(self, ast, c):
        self.checkUnreach(ast, c)
        ref = self.visit(ast.body, c)
        if(ast.op == "-"):
            if not isinstance(ref, (IntType, IntLiteral, FloatType, FloatLiteral)):
                raise TypeMismatchInExpression(ast)
            else:
                if isinstance(ref, Type):
                    return ref
                else:        
                    ref.value = -ref.value
                    return ref
        else:
            if not isinstance(ref, (BoolType, BooleanLiteral)):
                raise TypeMismatchInExpression(ast)
            else:
                if isinstance(ref, Type):
                    return ref
                else:
                    ref.value = not ref.value
                    return ref
            
    def visitBinaryOp(self, ast, c):
        self.checkUnreach(ast, c)
        opeRight = self.visit(ast.right, c)
        if ast.op != "=":
            opeLeft = self.visit(ast.left, c)
            checkLiteral = isinstance(opeLeft, Literal) and isinstance(opeRight, Literal)
            checkFlagString = isinstance(opeLeft, (StringType, StringLiteral)) or isinstance(opeRight, (StringType, StringLiteral))
            checkFlagBool = isinstance(opeLeft, (BoolType, BooleanLiteral)) or isinstance(opeRight, (BoolType, BooleanLiteral))
            checkFlagFloat = isinstance(opeLeft, (FloatType, FloatLiteral)) or isinstance(opeRight, (FloatType, FloatLiteral))
            checkFlagInt = isinstance(opeLeft, (IntType, IntLiteral)) or isinstance(opeRight, (IntType, IntLiteral))
            if checkFlagString or isinstance(opeLeft, VoidType) or isinstance(opeRight, VoidType):
                raise TypeMismatchInExpression(ast)
        if ast.op in {"+", "-", "*"}:
            if checkFlagBool:
                raise TypeMismatchInExpression(ast)
            elif checkFlagFloat:
                if checkLiteral:
                    return FloatLiteral(ope[ast.op](opeLeft.value, opeRight.value))
                else:
                    return FloatType()
            else:
                if checkLiteral:
                    return IntLiteral(ope[ast.op](opeLeft.value, opeRight.value))
                else:
                    return IntType()
        elif ast.op == "/":
            if checkFlagBool:
                raise TypeMismatchInExpression(ast)
            elif checkFlagFloat:
                if checkLiteral:
                    return FloatLiteral(ope[ast.op](opeLeft.value, opeRight.value))
                else:
                    return FloatType()
            else:
                if checkLiteral:
                    return IntLiteral(ope["//"](opeLeft.value, opeRight.value))
                else:
                    return IntType()
        elif ast.op == "%":
            if checkFlagBool or checkFlagFloat:
                raise TypeMismatchInExpression(ast)
            else:
                if checkLiteral:
                    return IntLiteral(ope["%"](opeLeft.value, opeRight.value))
                else:
                    return IntType()
        elif ast.op in {"<", "<=", ">", ">=", "!=", "=="}:
            if checkFlagFloat and ast.op in {"!=", "=="}:
                raise TypeMismatchInExpression(ast)
            if checkFlagBool and ast.op in {"<", "<=", ">", ">="}:
                raise TypeMismatchInExpression(ast)
            if checkFlagBool and (checkFlagFloat or checkFlagInt):
                raise TypeMismatchInExpression(ast)
            else:
                if checkLiteral:
                    return BooleanLiteral(ope[ast.op](opeLeft.value, opeRight.value))
                else:
                    return BoolType()
        elif ast.op == "&&" or ast.op == "||":
            if checkFlagFloat or checkFlagInt:
                raise TypeMismatchInExpression(ast)
            else:
                if checkLiteral:
                    return BooleanLiteral(ope[ast.op](opeLeft.value, opeRight.value))
                else:
                    return BoolType()
        else:
            if not isinstance(ast.left, ArrayCell):
                if isinstance(ast.left, (UnaryOp, BinaryOp, Literal, CallExpr)):
                    raise NotLeftValue(ast.left)
                elif isinstance(ast.left, Id):
                    index = []
                    check = False
                    ref = self.lookup(ast.left.name, reduce(lambda x,y: x + y, c[1:-1], c[0]), lambda x: x.name)
                    if ref is None:
                        raise Undeclared(Identifier(), ast.left.name)
                    for x in c[:-1]:
                        ref = self.lookup(True, x, lambda y: (y.name == ast.left.name) and not isinstance(y.mtype, MType))
                        if ref is not None:
                            if isinstance(ref.mtype, (ArrayType, ArrayPointerType)):
                                raise TypeMismatchInExpression(ast)
                            index.extend([c.index(x)])
                            index.extend([x.index(ref)])
                            check = True
                            break
                    if not check:
                        raise TypeMismatchInExpression(ast)
                    ref = c[index[0]][index[1]]
                    if isinstance(ref.mtype, BoolType):
                        if not isinstance(opeRight, (BoolType, BooleanLiteral)):
                            raise TypeMismatchInExpression(ast)
                        else:
                            ref.value = 0
                            c[index[0]][index[1]] = ref
                            return BoolType()
                    elif isinstance(ref.mtype, StringType):
                        if not isinstance(opeRight, (StringType, StringLiteral)):
                            raise TypeMismatchInExpression(ast)
                        else:
                            ref.value = 0
                            c[index[0]][index[1]] = ref
                            return StringType()
                    elif isinstance(ref.mtype, IntType):
                        if not isinstance(opeRight, (IntType, IntLiteral)):
                            raise TypeMismatchInExpression(ast)
                        else:
                            ref.value = 0
                            c[index[0]][index[1]] = ref
                            return IntType()
                    else:
                        if not isinstance(opeRight, (IntType, IntLiteral, FloatType, FloatLiteral)):
                            raise TypeMismatchInExpression(ast)
                        else:
                            ref.value = 0
                            c[index[0]][index[1]] = ref
                            return FloatType()
            left = self.visit(ast.left, c)
            right = self.visit(ast.right, c)
            if isinstance(right, IntLiteral):
                right = IntType()
            elif isinstance(right, FloatLiteral):
                right = FloatType()
            elif isinstance(right, StringLiteral):
                right = StringType()
            elif isinstance(right, BooleanLiteral):
                right = BoolType()
            if type(left) != type(right):
                if not (isinstance(left, FloatType) and isinstance(right, IntType)):
                    raise TypeMismatchInExpression(ast)
            return left

    def visitArrayCell(self, ast, c):
        self.checkUnreach(ast, c)
        ref = self.visit(ast.arr, c)
        refIdx = self.visit(ast.idx, c)
        if not isinstance(ref, (ArrayType, ArrayPointerType)) or not isinstance(refIdx, (IntType, IntLiteral)):
            raise TypeMismatchInExpression(ast)
        else:
            if isinstance(refIdx, IntLiteral) and isinstance(ref, ArrayType):
                if ((refIdx.value < 0) or (refIdx.value >= ref.dimen)):
                    raise IndexOutOfRange(ast) 
            return self.visit(ast.arr, c).eleType

    def visitIntLiteral(self, ast, c):
        self.checkUnreach(ast, c)
        return IntLiteral(ast.value)
    def visitBooleanLiteral(self, ast, c):
        self.checkUnreach(ast, c)
        return BooleanLiteral(ast.value)
    def visitFloatLiteral(self, ast, c):
        self.checkUnreach(ast, c)
        return FloatLiteral(ast.value)
    def visitStringLiteral(self, ast, c):
        self.checkUnreach(ast, c)
        return StringLiteral(ast.value)
    def visitIntType(self, ast, c):
        return IntType()
    def visitBoolType(self, ast, c):
        return BoolType()
    def visitFloatType(self, ast, c):
        return FloatType()
    def visitStringType(self, ast, c):
        return StringType()
    


