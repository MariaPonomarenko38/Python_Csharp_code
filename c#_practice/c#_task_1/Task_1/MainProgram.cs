using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;

namespace Task_1
{

    class MainProgram
    {
        static void Main(string[] args)
        {
            Collection ls = new Collection();
            string file_name = Input.ValidateFileName();
            ls.FillCollectionFile(file_name);
            while (true)
            {
                Console.WriteLine(@"Input number of option:
    1. Search meetings with value
    2. Sort by parametr
    3. Delete meeting by ID
    4. Add meeting
    5. Edit meeting by ID
    6. See all meetings
    7. Exit");
                string num = Console.ReadLine();
                string val = "";
                if(num.All(char.IsDigit) == false)
                {
                    Console.WriteLine("Number should contain digits!");
                    continue;
                }
                if (Int32.Parse(num) >= 1 && Int32.Parse(num) < 5)
                {
                    Console.WriteLine("Type value: ");
                    val = Console.ReadLine();
                }
                if (num == "1")
                {
                    ls.Search(val);
                }
                else if (num == "2")
                {
                    ls.Sort(val);
                }
                else if (num == "3")
                {
                    ls.Remove(val, file_name);
                }
                else if (num == "4")
                {
                    ls.AddTo(val, file_name);
                }
                else if (num == "5")
                {
                    Console.WriteLine("Type id:");
                    string id = Console.ReadLine();
                    Console.WriteLine("Type value: ");
                    val = Console.ReadLine();
                    ls.Edit(id, val, file_name);
                }
                else if (num == "6")
                {
                    ls.Print();
                }
                else
                {
                    break;
                }
            }
        }
    }
}