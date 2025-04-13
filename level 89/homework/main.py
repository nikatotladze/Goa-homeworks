# 1

# 1. Initialization (Constructor) - __init__ მეთოდი ქმნის ობიექტის ინიციალიზაციას


# 2. Class variables - გაზიარებული ცვლადები ყველა ობიექტისთვის


# 3. Instance methods - მეთოდები, რომლებიც მუშაობენ კონკრეტულ ობიექტთან


# 4. Inheritance - მემკვიდრეობა, როცა ერთი კლასი მიღებს მეორის თვისებებს


# 5. Multiple Inheritance - ობიექტი მემკვიდრეობს რამდენიმე კლასისგან


# 6. Multilevel Inheritance - მემკვიდრეობა რამდენიმე დონეზე


# 8. Abstract Classes - კლასი, რომელიც შეიცავს აბსტრაქტულ მეთოდს და ვერ შეიქმნება პირდაპირ


# 9. Polymorphism - ერთიდაიგივე მეთოდს სხვადასხვანაირი ქცევა სხვადასხვა კლასში


# 10. Duck Typing - ობიექტის ტიპი მნიშვნელობა არ აქვს, მთავარია აქვს თუ არა საჭირო მეთოდი


# 11. Aggregation - ერთი ობიექტის მეორეში ჩასმა ისე, რომ დამოუკიდებლადაც არსებობდეს


# 12. Composition - როცა კლასის სიცოცხლე დამოკიდებულია მეორე კლასზე


# 13. Static Methods - კლასზე არ არის დამოკიდებული, ობიექტზე არ უნდა გამოიძახო


# 14. Class Methods - კლასის დონეზე მუშაობს და cls არგუმენტი იყენებს


# 15. Data Hiding - ინფორმაციის დამალვა (name mangling)


# 2

# 1

# const getChar = String.fromCharCode;

# 2

# function checkAlive(health) {
#  return health > 0;
# }

# 3

# function combat(health, damage) {
#	return health < damage ? 0 : health - damage
# }

# 4

# function howManyLightsabersDoYouOwn(name) {
#  return name === 'Zach' ? 18 : 0;
# }

# 5

# function stringy(size) {
#  var str=''; 
#  for( var i=1; i<=size; i++ )
#    str+=i%2;
#  return str;
# }

# 6

# function mergeArrays(arr1, arr2) {
#  return Array.from(new Set(arr1.concat(arr2).sort((a,b) => (a-b))));
# }

# 7

# function mouthSize(animal) {
#  return animal.toLowerCase() == 'alligator' ? 'small' : 'wide';
# }

# 8

# function distinct(a) {
#  return [...new Set(a)];
# }

# 9

# function nthEven(n){
#  return (n-1)*2;
# }

# 10

# function twiceAsOld(dadYearsOld, sonYearsOld) {
#  return Math.abs(dadYearsOld - 2 * sonYearsOld);
# }
