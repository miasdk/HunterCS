//insert operation for unordered_map 
// unordered_map::insert
#include <iostream>
#include <string>
#include <unordered_map>

int main ()
{
  std::unordered_map<std::string,double>
              myrecipe,
              mypantry = {{"milk",2.0},{"flour",1.5}};

  std::pair<std::string,double> myshopping ("baking powder",0.3);

  myrecipe.insert (myshopping);                        // copy insertion
  myrecipe.insert(std::make_pair("sugar",1.0));            // move insertion
  std::cout << "myrecipe contains:" << std::endl;
  for (auto& x: myrecipe)
    std::cout << x.first << ": " << x.second << std::endl;

  std::cout << std::endl;
  return 0;
}