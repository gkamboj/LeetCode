class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int num = i + 1;
            String val = num % 15 == 0 ? "FizzBuzz" : (num % 5 == 0 ? "Buzz" : (num % 3 == 0 ? "Fizz" : String.valueOf(num)));
            result.add(val);
        }
        return result;
    }
}