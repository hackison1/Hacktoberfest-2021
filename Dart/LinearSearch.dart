void main() {
   print("Enter the limit: ");
   int limit = int.parse(stdin.readLineSync()!);
   List<int> values = [];
   print("Enter $limit numbers: ");
   for (var i = 0; i < limit; i++) {
      values.add(int.parse(stdin.readLineSync()!));
   }
   print("Enter the number to search: ");
   int s = int.parse(stdin.readLineSync()!);
   int flag = 0;
   values.asMap().forEach((index, value) {
      if (s == value) {
         print("$s found at index $index");
         flag = 1;
         return;
      }
   });
   if (flag == 0) {
      print("$s not found in the above list");
   }
}
