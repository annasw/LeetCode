class Solution {
    // oh god i haven't written in java for so long
    // this is probably all immature and bad
    // don't judge me it's been like six years since i wrote seriously in java
    public List<String> fizzBuzz(int n) {
        ArrayList<String> numbers = new ArrayList<String>();
        for (int i=1; i<=n; i++) {
            if (i%3==0 && i%5==0) {
                numbers.add(i-1, "FizzBuzz");
            }
            else if (i%3==0) {
                numbers.add(i-1, "Fizz");
            }
            else if (i%5==0) {
                numbers.add(i-1, "Buzz");
            }
            else {
                numbers.add(i-1, Integer.toString(i));
            }
        }
        return numbers;
    }
}
