// Creating Class named Inst
class Inst {
  // Declaring instance variable
  late int a;
  late int b;

  // Creating instance method name
  // sum with two parameters
  void sum(int c, int d) {
    // Using this to set the values of the
    // input to instance variable
    this.a = c;
    this.b = d;

    // Printing the result
    print('Sum of numbers is ${a + b}');
  }
}

void main() {
  // Creating instance of the class Inst(Creating Object)
  Inst abc = new Inst();

  // Calling the method sum with the use of object
  abc.sum(21, 12);
}
