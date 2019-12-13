import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):


    def test_Redeclared_Variable_1(self):
        input = """
                int something;
                float anything;
                void main(){return;}
                boolean main;
                """
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_Redeclared_Variable_2(self):
        input = """
                int anything[999];
                float anything;
                void main(string main[]){
                    // Nothing
                }
                boolean notMain;
                """
        expect = "Redeclared Variable: anything"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_Redeclared_Variable_3(self):
        input = """
                int something;
                float anything;
                void main(int same[]){
                    float same;
                }
                boolean notMain;
                """
        expect = "Redeclared Variable: same"
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_Redeclared_Variable_4(self):
        input = """
                int something;
                float anything;
                void main(int same[]){
                    main;
                    int main;
                    string main;
                }
                boolean notMain;
                """
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_Redeclared_Variable_5(self):
        input = """
                int something[999];
                float anything[999];
                void main(string main[]){
                    int scope;
                    float scope1;
                    {
                        string scope;
                        {
                            boolean scope;
                        }
                    }
                    boolean scope1;
                }
                boolean notMain;
                """
        expect = "Redeclared Variable: scope1"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_Redeclared_Function_1(self):
        input = """
                int someone;
                float anyone;
                boolean main;
                void main(){}
                """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_Redeclared_Function_2(self):
        input = """
                int someone;
                float anyone;
                boolean same;
                void main(){}

                int main(string d[]){return someone;}
                """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_Redeclared_Parameter(self):
        input = """
                int One;
                float Two;
                string Three;
                boolean Four;
                void Five(int One, float Two, string Three, boolean Four, int One[]){}
                int main(int One[]){
                    Five(1, 2., "Three", true, One);
                    return 1;
                }
                """
        expect = "Redeclared Parameter: One"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_No_Entry_Point_1(self):
        input = """
                int someone;
                string anyone;
                boolean main;
                float something;
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_No_Entry_Point_2(self):
        input = """
                int someone;
                string anyone;
                boolean main[999];
                float something;
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_Mismatch_Statement_If_1(self):
        input = """
                float many[99];
                boolean condition[99];
                int main(int argc){
                    if(true){
                        if(condition[0]){
                            // Just empty
                            return argc;
                        }
                    }else{
                        if(many[98] + 3){
                            // We have a exception
                            return argc + 3;
                        }
                    }
                }
                """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,ArrayCell(Id(many),IntLiteral(98)),IntLiteral(3)),Block([Return(BinaryOp(+,Id(argc),IntLiteral(3)))]))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_Mismatch_Statement_If_2(self):
        input = """
                int many[99];
                boolean condition[99];
                int main(int argc){
                    if(true){
                        if((many[98] <= 3) && (argc == argc + 1)){
                            // Just empty
                            return argc;
                        }
                    }else{
                        if(many[98] = 3){
                            // We have a exception
                            return argc;
                        }
                    }
                    return argc;
                }
                """
        expect = "Type Mismatch In Statement: If(BinaryOp(=,ArrayCell(Id(many),IntLiteral(98)),IntLiteral(3)),Block([Return(Id(argc))]))"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_Mismatch_Statement_If_3(self):
        input = """
                int many[99];
                boolean condition[99];
                int main(int argc){
                    if(BooleanFunction()){
                        if((many[98] <= 3) && (argc == argc + 1)){
                            return argc;
                        }
                    }else{
                        if(ArrayFunction()){
                            return argc + 3;
                        }
                    }
                }
                boolean BooleanFunction(){return true;}
                void ArrayFunction(){return;}
                """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(ArrayFunction),[]),Block([Return(BinaryOp(+,Id(argc),IntLiteral(3)))]))"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_Mismatch_Statement_For_1(self):
        input = """
                float many;
                string main(int man){
                    for(man = 0; many <= man; man = man + 1){
                        for(true; true; true){
                            print("Upin Ipin >.<");
                        }
                    }
                    return "Nothing";
                }

                void print(string str){
                    print(str);
                }
                """
        expect = "Type Mismatch In Statement: For(BooleanLiteral(true);BooleanLiteral(true);BooleanLiteral(true);Block([CallExpr(Id(print),[StringLiteral(Upin Ipin >.<)])]))"
        self.assertTrue(TestChecker.test(input,expect,414))
    
    def test_Mismatch_Statement_For_2(self):
        input = """
                float many;
                string main(int man){
                    for(man = 0; many <= man; man = man + 1){
                        for(man; wrong(); man){
                            print("Upin Ipin >.<");
                        }

                        for(1; 2; 3){
                            print("It's wrong");
                        }
                    }
                    return "Nothing";
                }

                void print(string str){
                    print(str);
                }

                boolean wrong(){
                    return false;
                }
                """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);IntLiteral(2);IntLiteral(3);Block([CallExpr(Id(print),[StringLiteral(It's wrong)])]))"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_Mismatch_Statement_DoWhile_1(self):
        input = """
                string str;
                boolean bool[99];
                boolean[] main(){
                    for(3; wrong(); 3){
                        do
                            str = "ABC";
                            print(str);
                        while(bool);
                        return bool;
                    }
                }
                void print(string str){
                    print(str);
                }

                boolean wrong(){
                    return false;
                }
                """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(str),StringLiteral(ABC)),CallExpr(Id(print),[Id(str)])],Id(bool))"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_Mismatch_Statement_DoWhile_2(self):
        input = """
                string str;
                boolean bool[99];
                boolean[] main(boolean input[]){
                    do
                        do 
                        {
                            return input;
                        }
                        while(bool[0] && true || false);
                    while(str);
                }

                boolean wrong(){
                    return false;
                }
                """
        expect = "Type Mismatch In Statement: Dowhile([Dowhile([Block([Return(Id(input))])],BinaryOp(||,BinaryOp(&&,ArrayCell(Id(bool),IntLiteral(0)),BooleanLiteral(true)),BooleanLiteral(false)))],Id(str))"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_Mismatch_Statement_Return_1(self):
        input = """
                string str;
                boolean bool[99];
                void main(int para){
                    {
                        {
                            return para;
                        }
                    }
                }
                """
        expect = "Type Mismatch In Statement: Return(Id(para))"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_Mismatch_Statement_Return_2(self):
        input = """
                string str;
                boolean bool[99];
                float main(int para){
                    if(true){
                        return para;
                    }
                    else{
                        if(false){
                            return 3.;
                        }
                    }
                    return str;
                }
                """
        expect = "Type Mismatch In Statement: Return(Id(str))"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_Mismatch_Statement_Return_3(self):
        input = """
                string str[999];
                boolean bool[99];
                string[] main(string char[]){
                    if(false){
                        return str;
                    }
                    else{
                        if(bool[98]){
                            return char;
                        }
                        else{
                            return bool[98];
                        }
                    }
                }
                """
        expect = "Type Mismatch In Statement: Return(ArrayCell(Id(bool),IntLiteral(98)))"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_Mismatch_Expression_ArrayCell_1(self):
        input = """
                int first;
                float second;
                boolean third[999];
                void main(string str){
                    for(first = 0; first < second; first = first + 1){
                        (second + first)[99] = true;
                    }
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(BinaryOp(+,Id(second),Id(first)),IntLiteral(99))"
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_Mismatch_Expression_ArrayCell_2(self):
        input = """
                int first;
                float second;
                void main(string str){
                    for(first = 0; first < second; first = first + 1){
                        (array())[num() / 3] = 3;
                        (array())[num() + second / 3] = 3;
                    }
                }
                int[] array(){
                    int input[3];
                    if(first < 3){
                        return input;
                    }
                    return input;
                }

                int num(){
                    return first + 1;
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(array),[]),BinaryOp(+,CallExpr(Id(num),[]),BinaryOp(/,Id(second),IntLiteral(3))))"
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_Mismatch_Expression_ArrayCell_3(self):
        input = """
                int first;
                float second;
                boolean array[1000];
                string another[1000];
                string main(string str){
                    do{
                        array[first / 3] = (array[Return(Return(Return(Return(1))))] == true);
                    }while(array[first]);
                    another[0] = second;
                    return "OK";
                }

                int Return(int a){
                    return a;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(another),IntLiteral(0)),Id(second))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_Mismatch_Expression_Binary_Unary_1(self):
        input = """
                int first;
                float second;
                void main(float third){
                    second = first;
                    second = second + third;
                    first = third;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(first),Id(third))"
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_Mismatch_Expression_Binary_Unary_2(self):
        input = """
                int first;
                float second;
                void main(string str){
                    if(true){
                        if(false){
                            second + str;
                            second + first;
                        }
                    }
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(second),Id(str))"
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_Mismatch_Expression_Binary_Unary_3(self):
        input = """
                int first;
                float second;
                void main(string str){
                    if(!true){
                        return;
                    }else{
                        if(getFloat() == 3.2) return;
                        else second = first + second;
                    }
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(==,CallExpr(Id(getFloat),[]),FloatLiteral(3.2))"
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_Mismatch_Expression_Binary_Unary_4(self):
        input = """
                string main(string str, int INT){
                    do{
                        -3;
                        print("Assignment 3");
                        print(-str);
                    }while(INT < 100);
                    return "OK";
                }

                void print(string s){
                    return;
                }
                """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(str))"
        self.assertTrue(TestChecker.test(input,expect,427))
    
    def test_Mismatch_Expression_Binary_Unary_5(self):
        input = """
                int left;
                float right;
                boolean[] main(){
                    boolean TRUE[99];
                    if(TRUE[0]){
                        left = round(right);
                    }else{
                        left = -right / 4;
                    }
                    return TRUE;
                }

                int round(float f){
                    int temp;
                    temp = round(f);
                    return temp;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(left),BinaryOp(/,UnaryOp(-,Id(right)),IntLiteral(4)))"
        self.assertTrue(TestChecker.test(input,expect,428))
    
    def test_Mismatch_Expression_Binary_Unary_6(self):
        input = """
                int left;
                float right;
                boolean[] main(){
                    boolean TRUE[99];
                    if(TRUE[0]){
                        left = round(right);
                    }else{
                        right = left = 4 * 3 / 2;
                    }
                    for(left; TRUE[5]; round(right)){
                        TRUE = (left * right) < 3 ;
                    }

                    return TRUE;
                }

                int round(float f){
                    int temp;
                    temp = round(f);
                    return temp;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(TRUE),BinaryOp(<,BinaryOp(*,Id(left),Id(right)),IntLiteral(3)))"
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_Mismatch_Expression_Binary_Unary_7(self):
        input = """
                int left;
                float right;
                string name;
                boolean[] main(){
                    boolean TRUE[99];
                    name = "My Name";
                    TRUE[3] = (getInt() != round(right));
                    TRUE[4] = left == right;
                    return TRUE;
                }

                int round(float f){
                    int temp;
                    temp = round(f);
                    return temp;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(left),Id(right))"
        self.assertTrue(TestChecker.test(input,expect,430))
    
    def test_Mismatch_Expression_Binary_Unary_8(self):
        input = """
                int left;
                float right;
                string name;
                float main(){
                    boolean TRUE;
                    TRUE = right < left;
                    left = right % left;
                    return right;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(right),Id(left))"
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test_Mismatch_Expression_Binary_Unary_9(self):
        input = """
                float one;
                float main(){
                    one =  -(-one * getFloat() - 3.2 / 4 + Floating(Floating(Floating(one))));
                    if(true && false){
                        // do nothing
                    }else{
                        if(true >= false){
                            return 3;
                        }
                    }
                    return one;
                }

                float Floating(float f){
                    return f;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(true),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,432))
    
    def test_Mismatch_Expression_Binary_Unary_10(self):
        input = """
                float one[2];
                float[] main(){
                    one[0] =  -(-one[0] * getFloat() - 3.2 / 4 + Floating(Floating(Floating(one[0]))));
                    if(true && false){
                        one[1] = 3;
                    }else{
                        if(true || !false){
                            one = one[1];
                        }
                    }
                    return one;
                }

                float Floating(float f){
                    return f;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(one),ArrayCell(Id(one),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test_Mismatch_Expression_Binary_Unary_11(self):
        input = """
                boolean TRUE[999];
                string STR[999];
                boolean[] main(string s){
                    if(TRUE[99] == false){
                        TRUE[99] = true;
                    }else{
                        if(true || !false){
                            STR[99] = s;
                        }
                        TRUE[99] = STR[99];
                    }
                    return one;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(TRUE),IntLiteral(99)),ArrayCell(Id(STR),IntLiteral(99)))"
        self.assertTrue(TestChecker.test(input,expect,434))
    
    def test_Mismatch_Expression_Binary_Unary_12(self):
        input = """
                boolean TRUE[999];
                string STR[999];
                void main(string s){
                    if(TRUE[99] == TRUE[90]){
                        TRUE[99] = TRUE[998];
                    }else{
                        if(true || !false){
                            STR[99] = s;
                        }
                        TRUE[99] = true || main(STR[99]);
                    }
                    return one;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(||,BooleanLiteral(true),CallExpr(Id(main),[ArrayCell(Id(STR),IntLiteral(99))]))"
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def test_Mismatch_Expression_CallExpr_1(self):
        input = """
                int func(){
                    return 1;
                }

                void main(){
                    func(func());
                    // We have an error
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[CallExpr(Id(func),[])])"
        self.assertTrue(TestChecker.test(input,expect,436))
    
    def test_Mismatch_Expression_CallExpr_2(self):
        input = """
                int func(int a, float b, boolean c, string d){
                    return 1;
                }

                void main(){
                    func(1, 1.1, true, "OK");
                    // Still ok here
                    func(1, 1.1, true);
                    // Missing a parameter
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[IntLiteral(1),FloatLiteral(1.1),BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test_Mismatch_Expression_CallExpr_3(self):
        input = """
                int func(int a, float b, boolean c, string d){
                    return 1;
                }

                void main(){
                    func(1, 1.1, true, "OK");
                    // Still ok here
                    func(1, 1.1, true, "OK", 1, 1.1, true, "OK");
                    // Too muchhhhhhhh
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[IntLiteral(1),FloatLiteral(1.1),BooleanLiteral(true),StringLiteral(OK),IntLiteral(1),FloatLiteral(1.1),BooleanLiteral(true),StringLiteral(OK)])"
        self.assertTrue(TestChecker.test(input,expect,438))
    
    def test_Mismatch_Expression_CallExpr_4(self):
        input = """
                int func(int a, float b, boolean c, string d){
                    return 1;
                }

                void main(){
                    //func(1, 1.1, true, "OK");
                    //func(1, 1, false, "FALSE");
                    func(1.1, 1, false, "FAILED");
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[FloatLiteral(1.1),IntLiteral(1),BooleanLiteral(false),StringLiteral(FAILED)])"
        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test_Mismatch_Expression_CallExpr_5(self):
        input = """
                int func(int a, float b, boolean c, string d, int A[], float B[], boolean C[], string D[]){
                    return 1;
                }

                void main(){
                    int A[99];
                    float B[99];
                    boolean C[99];
                    string D[99];
                    func(0, 0, false, "FAILED", A, B, C, D);
                    func(0, 0, false, "FAILED", A, A, C, D);
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[IntLiteral(0),IntLiteral(0),BooleanLiteral(false),StringLiteral(FAILED),Id(A),Id(A),Id(C),Id(D)])"
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test_Mismatch_Expression_CallExpr_6(self):
        input = """
                string[] func(int a, float b, boolean c, string d, int A[], float B[], boolean C[], string D[]){
                    return D;
                }

                string[] main(int E[]){
                    int A[99];
                    float B[99];
                    boolean C[99];
                    string D[99];
                    func(0, 0, false, "FAILED", A, B, C, D);
                    func(0, 0, false, "FAILED", E, B, C, D);
                    func(0, 0, false, "FAILED", 0, 0, false, "FAILED");
                    return func(0, 0, false, "FAILED", A, B, C, D);
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[IntLiteral(0),IntLiteral(0),BooleanLiteral(false),StringLiteral(FAILED),IntLiteral(0),IntLiteral(0),BooleanLiteral(false),StringLiteral(FAILED)])"
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test_Function_Not_Return_1(self):
        input = """
                int main(int i){
                    for(i = 0; i < 3; i = i + 1){
                        // Just doing stuff
                    }

                    if(true){
                        i = i * 1;
                    }else{
                        // Still doing stuff
                        // Still not return
                    }
                    // OK not return
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,442))
    
    def test_Function_Not_Return_2(self):
        input = """
                void main(int i){
                    for(i = 0; i < 3; i = i + 1){
                        return;
                    }

                    if(true){
                        i = i * 1;
                    }else{
                        // Still doing stuff
                        // Still not return
                    }
                }

                int MAIN(){
                    if(true){
                        return 1;
                    }
                }
                """
        expect = "Function MAIN Not Return "
        self.assertTrue(TestChecker.test(input,expect,443))
    
    def test_Function_Not_Return_3(self):
        input = """
                int main(int i){
                    for(i = 0; i < 3; i = i + 1){
                        return 1;
                    }

                    if(true){
                        return 1;
                    }else{
                    }
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test_Function_Not_Return_4(self):
        input = """
                int main(int i){
                    if(true){
                        if(true){
                            if(true){
                                return 1;
                            }
                            return 1;
                        }
                        return 1;
                    }
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_Function_Not_Return_5(self):
        input = """
                int main(int i){
                    if(true){
                        if(true){
                            if(true){
                                return 1;
                            }
                            return 1;
                        }
                        return 1;
                    }else{
                        if(false){
                            if(false){
                                return 1;
                            }
                        }else{
                            return 1;
                        }
                    }
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_Function_Not_Return_6(self):
        input = """
                int main(int i){
                    for(1; true; 1){
                        if(true) return 1;
                        else return 1;
                    }

                    return 1;
                }

                float MAIN(){
                    for(1; true; 1){
                        if(true) return 1;
                    }
                }
                """
        expect = "Function MAIN Not Return "
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_Function_Not_Return_7(self):
        input = """
                int main(int i){
                    {
                        {
                            {
                                {
                                    do
                                        return 1;
                                    while(false);
                                }
                            }
                        }
                    }
                }

                float MAIN(){
                    {
                        {
                            {
                                {
                                    {
                                        if(true) return 1;
                                    }
                                }
                            }
                        }
                    }
                }
                """
        expect = "Function MAIN Not Return "
        self.assertTrue(TestChecker.test(input,expect,448))
    
    def test_Not_In_Loop_1(self):
        input = """
                void main(int i){
                    {
                        {
                            {
                                {
                                    do
                                        i = i + 1;  
                                    while(false);
                                    break;
                                }
                            }
                        }
                    }
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,449))
    
    def test_Not_In_Loop_2(self):
        input = """
                void main(int i){
                    for(1; true; 1){
                        {
                            {
                                do{

                                }
                                while(true);
                                break;
                            }
                        }
                    }
                    continue;
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,450))
    
    def test_Not_In_Loop_3(self):
        input = """
                void main(int i){
                    for(1; true; 1){
                        // Yeah...
                    }

                    for(1; true; 1){
                        // Okay...
                    }
                    continue;
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test_Not_In_Loop_4(self):
        input = """
                void main(int i){
                    for(1; true; 1){
                        for(1; true; 1){
                            for(1; true; 1){
                                for(1; true; 1){
                                    break;
                                }
                                break;
                            }
                            break;
                        }
                        continue;
                    }
                    continue;
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,452))
    
    def test_Unreachable_Function_1(self):
        input = """
                int func(){
                    return func();
                }
                void main(int i){
                    // Not calling func
                }
                """
        expect = "Unreachable Function: func"
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test_Unreachable_Function_2(self):
        input = """
                int func(){
                    return func1();
                }

                int func1(){
                    return func2();
                }

                int func2(){
                    return 1;
                }

                void main(int i){
                    // Not calling func
                }
                """
        expect = "Unreachable Function: func"
        self.assertTrue(TestChecker.test(input,expect,454))
    
    def test_Unreachable_Function_3(self):
        input = """
                int func(){
                    return func1();
                }

                int func1(){
                    return func();
                }

                void main(int i){
                    // Not calling MAIN
                }

                void MAIN(){

                }
                """
        expect = "Unreachable Function: MAIN"
        self.assertTrue(TestChecker.test(input,expect,455))
    
    def test_Not_Left_Value_1(self):
        input = """
                void main(){
                    int a, b;
                    a = 0;
                    b = 0;
                    -b = a;
                }
                """
        expect = "Not Left Value: UnaryOp(-,Id(b))"
        self.assertTrue(TestChecker.test(input,expect,456))
    
    def test_Not_Left_Value_2(self):
        input = """
                void main(){
                    int first, second;
                    first = 1 + 3 * 4 / 5 - 6;
                    second = 5 + 6 * 7 / 30;
                    first= 5 * 6 + 29 = 56;
                }
                """
        expect = "Not Left Value: BinaryOp(+,BinaryOp(*,IntLiteral(5),IntLiteral(6)),IntLiteral(29))"
        self.assertTrue(TestChecker.test(input,expect,457))
    
    def test_Not_Left_Value_3(self):
        input = """
                void main(int bool[]){
                    int first, second;
                    first = 1 + 3 * 4 / 5 - 6;
                    second = 5 + 6 * 7 / 30;
                    first * second = first + second;
                }
                """
        expect = "Not Left Value: BinaryOp(*,Id(first),Id(second))"
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_Not_Left_Value_4(self):
        input = """
                void main(int bool[]){
                    int first, second;
                    first = 1 + 3 * 4 / 5 - 6;
                    second = 5 + 6 * 7 / 30;
                    func() = first + second;
                }

                int func(){
                    return 1;
                }
                """
        expect = "Not Left Value: CallExpr(Id(func),[])"
        self.assertTrue(TestChecker.test(input,expect,459))
    
    def test_Not_Left_Value_5(self):
        input = """
                void main(int bool[]){
                    int first, second;
                    first = 1 + 3 * 4 / 5 - 6;
                    second = 5 + 6 * 7 / 30;
                    1 + 2 + 3 + 4 + 5 = first = first + second;
                }
                """
        expect = "Not Left Value: BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,460))
    
    def test_Unreachable_Statement_1(self):
        input = """
                int main(int i){
                    for(i; i < 3; i = i + 1){
                        return 1; 
                        // Not yet
                    }

                    if(true){
                        return 1;
                        // Still not yet
                    }

                    return 1;
                    // Now 
                    i;
                }
                """
        expect = "Unreachable Statement: Id(i)"
        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test_Unreachable_Statement_2(self):
        input = """
                int main(int i){
                    if(true){
                        i = i + 1;
                        i = i / 2 * 3 + 4;
                        return 1;
                    }else{
                        if(false){
                            i = i * 2;
                            return 1;
                        }else{
                            i = 0;
                            return 1;
                            i = 1;
                        }
                    }
                }
                """
        expect = "Unreachable Statement: BinaryOp(=,Id(i),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_Unreachable_Statement_3(self):
        input = """
                int main(int i){
                    if(true){
                        i = i + 1;
                        i = i / 2 * 3 + 4;
                        return 1;
                    }else{
                        if(false){
                            i = i * 2;
                            return 1;
                        }else{
                            {
                                {
                                    {
                                        {
                                            {
                                                return 1;
                                            }
                                        }
                                    }
                                    int a, b, c, d, e;
                                    int a1, b1, c1, d1, e1;
                                    int a2, b2, c2, d2, e2;
                                    // Here
                                    a = 0;
                                }
                            }
                        }
                    }
                }
                """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,463))
    
    def test_Unreachable_Statement_4(self):
        input = """
                int main(int i){
                    for(i; i < i; i){
                        return 1;
                        {
                        }
                    }
                    return 1;
                }
                """
        expect = "Unreachable Statement: Block([])"
        self.assertTrue(TestChecker.test(input,expect,464))
    
    def test_Unreachable_Statement_5(self):
        input = """
                int main(int i){
                    for(i; i < i; i){
                        if(true){
                            return 1;
                        }else{
                            return 1;
                        }
                        int a;
                        int b;
                        int c;
                        int d;
                        return 3;
                    }
                    return 1;
                }
                """
        expect = "Unreachable Statement: Return(IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,465))
    
    def test_Unreachable_Statement_6(self):
        input = """
                int main(int i){
                    for(i; i < i; i){
                        for(i; i < i; i){
                            if(true){
                                break;
                            }else{
                                continue;
                            }
                            break;
                        }
                    }
                    return 1;
                }
                """
        expect = "Unreachable Statement: Break()"
        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test_Unreachable_Statement_7(self):
        input = """
                int main(int i){
                    for(i; i < i; i){
                        for(i; i < i; i){
                            if(true){
                                i = i % 1;
                                i = i + 1;
                            }else{
                                continue;
                            }
                            break;
                            continue;
                        }
                    }
                    return 1;
                }
                """
        expect = "Unreachable Statement: Continue()"
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def test_Unreachable_Statement_8(self):
        input = """
                int main(int i){
                    for(i; i < i; i){
                        for(i; i < i; i){
                            if(true){
                                i = i % 1;
                                i = i + 1;
                                continue;
                                int a;
                                int b;
                                int c;
                                int d;
                            }else{
                                // Nothing
                            }
                            break;
                        }
                        continue;
                        return 1;
                    }
                    return 1;
                }
                """
        expect = "Unreachable Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,468))
    
    def test_Unreachable_Statement_9(self):
        input = """
                int main(int i){
                    for(i; i < i; i){
                        for(i; i < i; i){
                            break;
                            if(true){
                                i = i % 1;
                                i = i + 1;
                                continue;
                                int a;
                                int b;
                                int c;
                                int d;
                            }else{
                                // Nothing
                            }
                            break;
                        }
                        continue;
                    }
                    return 1;
                }
                """
        expect = "Unreachable Statement: If(BooleanLiteral(true),Block([BinaryOp(=,Id(i),BinaryOp(%,Id(i),IntLiteral(1))),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1))),Continue(),VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),VarDecl(d,IntType)]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,469))
    
    def test_Unreachable_Statement_10(self):
        input = """
                int main(int i){
                    for(i; i < i; i){
                        break;
                        for(i; i < i; i){
                            break;
                        }
                        continue;
                    }
                    return 1;
                }
                """
        expect = "Unreachable Statement: For(Id(i);BinaryOp(<,Id(i),Id(i));Id(i);Block([Break()]))"
        self.assertTrue(TestChecker.test(input,expect,470))
    
    def test_Index_Out_Of_Range_1(self):
        input = """
                int main(int i[]){
                    i[99999999] = i[99999] + 1;
                    // OK
                    int a[999];
                    a[000] = a[998] + 1;
                    return a[999];
                }
                """
        expect = "Index Out Of Range: ArrayCell(Id(a),IntLiteral(999))"
        self.assertTrue(TestChecker.test(input,expect,471))
    
    def test_Index_Out_Of_Range_2(self):
        input = """
                int main(int i[]){
                    i[99999999] = i[99999] + 1;
                    // OK
                    int a[999];
                    a[000] = a[998] + 1;
                    return a[999 - 1 + 1 / 1000 + 1];
                }
                """
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(-,IntLiteral(999),IntLiteral(1)),BinaryOp(/,IntLiteral(1),IntLiteral(1000))),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,472))
    
    def test_Index_Out_Of_Range_3(self):
        input = """
                int main(int i[]){
                    float a[0];
                    boolean b[999];
                    if(b[998] || false){
                        if(b[0] == true){
                            return 1;
                        }
                    }else{
                        a[0] = a[0] / 3;
                    }
                    return 1;
                }
                """
        expect = "Index Out Of Range: ArrayCell(Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,473))
    
    def test_Index_Out_Of_Range_4(self):
        input = """
                int main(int i[]){
                    float a[3];
                    boolean b[999];
                    if(b[998] || false){
                        if(b[0] == true){
                            return 1;
                        }
                    }else{
                        a[--------------------------------2] = a[-----------2] / 3;
                    }
                    return 1;
                }
                """
        expect = "Index Out Of Range: ArrayCell(Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLiteral(2)))))))))))))"
        self.assertTrue(TestChecker.test(input,expect,474))
    
    def test_Index_Out_Of_Range_5(self):
        input = """
                int main(int i[]){
                    float a[3];
                    boolean b[999];
                    if(b[998] || false){
                        if(b[0] == true){
                            return 1;
                        }
                        return 1;
                    }else{
                        a[2 - 3] = a[------------2] / 3;
                    }
                    return 1;
                }
                """
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(-,IntLiteral(2),IntLiteral(3)))"
        self.assertTrue(TestChecker.test(input,expect,475))
    
    def test_Uninitialized_Variable_1(self):
        input = """
                int main(int a){
                    int b;
                    a = b;
                    return 1;
                }
                """
        expect = "Uninitialized Variable: b"
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test_Uninitialized_Variable_2(self):
        input = """
                int main(int a[]){
                    int b;
                    b = 1;
                    a[b + 1] = b;
                    int c;
                    {
                        {
                            int c;
                            c = 1;
                        }
                    }
                    return a[c];
                }
                """
        expect = "Uninitialized Variable: c"
        self.assertTrue(TestChecker.test(input,expect,477))
    
    def test_Uninitialized_Variable_3(self):
        input = """
                int main(int a[]){
                    int b;
                    b = 1;
                    a[b + 1] = b;
                    int c;
                    {
                        int c;
                        {
                            int c;
                            c = 1;
                        }
                        c = 1;
                    }
                    return a[c];
                }
                """
        expect = "Uninitialized Variable: c"
        self.assertTrue(TestChecker.test(input,expect,478))
    
    def test_Uninitialized_Variable_4(self):
        input = """
                boolean global;
                int main(int a[]){
                    int b;
                    b = 1;
                    a[b + 1] = b;
                    int x;
                    {
                        string x;
                        {
                            {
                                {
                                    string x;
                                    {
                                        x = "OK";
                                    }
                                }
                            }
                        }
                        string b;
                        b = x;
                        // Uninitiliazed
                    }
                    return 1;
                }
                """
        expect = "Uninitialized Variable: x"
        self.assertTrue(TestChecker.test(input,expect,479))
    
    def test_Uninitialized_Variable_5(self):
        input = """
                boolean global;
                int main(int a[]){
                    int b;
                    b = 1;
                    a[b + 1] = b;
                    int c, d, e;
                    {
                        {
                            {
                                d = 1;
                                e = 1;
                            }
                        }
                    }
                    e = c + d;
                    return 1;
                }
                """
        expect = "Uninitialized Variable: c"
        self.assertTrue(TestChecker.test(input,expect,480))
    
    def test_Uninitialized_Variable_6(self):
        input = """
                boolean global;
                int main(){
	            	int a,b,c;
	            	a=b=3;
	            	putInt(b);
                    
	            	putInt(c);

	            	return getInt();
	            }
                """
        expect = "Uninitialized Variable: c"
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test_All_1(self):
        input = """
                float maximum(float a, float b, float c){
                    if (a > b)
                    {
                        if (a > c) return a;
                        else return c;
                    }
                    else{
                        if (b > c) return b;
                        else return c;
                        }
                }
                float minimum(float a, float b, float c)
                {
                    if (a < b)
                    {
                        if (a < c) return a;
                        else return c;
                    }
                    else {
                	    if (b < c) return b;
                        else return c;
                    }
                }
		        float main(int arcg, string arcv[]){
		        		return minimum(1, 1, 1) + maximum(1, 1, 1);
		        }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,482))
    
    def test_All_2(self):
        input = """
                int main(){
                    return GCD(6,9);
                }

                int GCD(int a, int b){
                    if (a == 0) return a;
                    else {
                        return GCD(a,b-a);
                    }
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,483))
    
    def test_All_3(self):
        input = """
                int test, statements;
                boolean all;
                void main(boolean thisTestcase){
                    for(test; all; statements)
                        if(thisTestcase == true)
                            do
                                "Yeah you nailed the statements";
                                break;
                            while(stillRunning());
                    printf("Congrats!");
                }

                void printf(string s){
                    printf(s);
                }

                boolean stillRunning(){
                    return all || false;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,484))
    
    def test_All_4(self):
        input = """
                int a, b;
                float c, d;
				boolean main(boolean exp){
                    if(a < b && b >= c && c > d)
                        doThis();
                    else
                        doThis();
                    return exp = (a < b) == (c > d);
                }

                int doThis(){
                    return 0;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))
    
    def test_All_5(self):
        input = """
                void main(int a[]){
                    funcall(a[9999]);
                    a[99] = funcall(funcall(a[funcall(a[funcall(1)])]));
                    return;
                }

                int funcall(int a){
                    return a;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,486))
    
    def test_All_6(self):
        input = """
                void main(int A, boolean B){
                    funcall(A, A + 1);
                    do
                        do
                            do
                                A = 1;
                                B = A > (A + 6.e-12);
                                break;
                            while(true);
                        while(true);
                    while(true);
                    return;
                }

                int funcall(int a, int b){
                    return a + b;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,487))
    
    def test_All_7(self):
        input = """
                int isInterrupt;
                int countNumber;
                //countNumber = 0;
                int interruptVector[0];
                int main(){
                    int count;
                    count = 0;
                    do{
                        if(countNumber % 3 == 0) return interruptVector[countNumber];
                        else
                            for(count; count < countNumber; countNumber)
                                countNumber = interruptVector[countNumber + count];
                        return 1;
                    }
                    while(true);
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488))
    
    def test_All_8(self):
        input = """
                int floor1,floor2,floor3,floor4,basement;
                void main(){
                    if(goDown(floor4))
                        if(goDown(floor3))
                            if(goDown(floor2))
                                if(goDown(floor1))
                                    if(goDown(basement))
                                        printf("Hello Annabelle!");
                                    else
                                        goUp();
                                else
                                    goUp();
                            else
                                goUp();
                        else
                            printf("You shouldn't go to the basement :)))");
                }

                boolean goDown(int floor){
                    return floor > basement;
                }

                void goUp(){
                    goUp();
                }

                void printf(string s){
                    printf(s);
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,489))
    
    def test_All_9(self):
        input = """
                void main(boolean stair){
                    stair = true;
                    letMakeAStair(true);
                    if(stair){
                        //do nothing
                    }
                    else
                        if(stair){
                            //do nothing}}}}}}
                        }
                        else
                            if(stair){
                                {// do nothing}
                            }}
                            else{
                                {// do nothing}
                }}}

                void letMakeAStair(boolean bool){
                    return;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_All_10(self):
        input = """
                float number1, number2;
                void main(){
                    int bePatient;
                    do
                        bePatient = 0;
                        bePatient = 1;
                        bePatient = 2;
                    if(bePatient > 3)
                        bePatient = bePatient + 1;
                    while(true);
                    do 
                        number1 = number1 + number2;
                    while(number1 > number2);
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,491))
    
    def test_All_11(self):
        input = """
                int timer[99];
                int timer0, timer1;
                int threshhold;
                boolean[] main(int i){
                    boolean TRUE[99];
                    if(timer0 == threshhold)
                        if(timer1 == threshhold)
                            for(i = 0; timer0 == threshhold; i = i + 1)
                                do
                                    timer0 = timer1 + timer[timer[timer[0]]];
                                while(timer0 != 0);
                        else
                            // Nothing
                        timer1 = 0;
                        return TRUE;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,492))
    
    def test_All_12(self):
        input = """
                void getSome(){
                    getSome();
                }
                
                string main(int a, string b, boolean c){
                    if(a == 3 && !c){
                        do
                            b = "Your name";
                            getSome();
                            getSome();
                            getSome();
                        while(true);
                    }
                    b = "Fine";
                    return b;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_All_13(self):
        input = """
                float main(){
                    return amIEmpty(1, true, 1);
                }


				float amIEmpty(int a, boolean smile, float difficult){
                    if(smile) 
                        return difficult = difficult / 2;
                    else
                        return difficult = difficult * 2;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,494))
    
    def test_All_14(self):
        input = """
                float hug;

                int Someone(float hug){
                    return 3000;
                }

                void main(int You){
                    if(true || false){
                        hug = 3000;
                        You = Someone(hug);
                    }
                    else
                        putStringLn("Have a good day!");
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))
    
    def test_All_15(self):
        input = """
                void main(){
                    if(true && false || !true)
                        if(beHumble())
                            if(beKind())
                                if(bePositive())
                                    putString("Yayyyyy");
                    else
                        putStringLn("Have a good day!");
                }

                boolean beHumble(){
                    return true;
                }

                boolean beKind(){
                    return true;
                }

                boolean bePositive(){
                    return true;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test_All_16(self):
        input = """
				void main(boolean free, boolean notFree,boolean busy){
                    do
                        do
                            do
                                do
                                    putStringLn("stop");
                                while(free);
                            while(free);
                        while(notFree);
                    while(busy == false);
				}
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,497))
    
    def test_All_17(self):
        input = """
                string statement1, statement2, statement3;
				void main(float infinity){
                    int i;
                    for(i = 3; i < infinity; i = i + 1)
                        do
                            statement1;
                            statement2;
                            statement3;
                        while(true);
                    int endline;
                    string line;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,498))
    
    def test_All_18(self):
        input = """
                int main(float infinity){
                    int i;
                    for(i = 3; i < infinity; i = i + 1){
                        for(i; i == i; i){
                            {//do nothing
                        }}
                        break;
                    }
                    return 1;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,499))
    
    def test_All_19(self):
        input = """
                int a;
                string main(boolean PPL){
                    funcall(a, a + 1);
                    if(PPL)
                        return "Runnnnnnnnnn";
                    else{
                        // Runnnnnnnnnnnnnnnnnnnnnnn
                    }
                    return "Still runnnnnnn";
                }

                int funcall(int a, int b){
                    return a + b;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,500))




    