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
            OnlineMeeting a = new OnlineMeeting("4;29.8.2021;08:09;20:25;http://aoom/49839gk483;Denver Maddox;Austin Bradley");
            a.Set("id", "8");
            Console.WriteLine(a);
            Collection ls = new Collection();
            Console.WriteLine("Write file name:");
            string file_name = Console.ReadLine();
            file_name = "C:/code/practice_uni/c#_practice/c#_task_1/Task_1/" + file_name;
            if (Input.ValidateFileName(file_name) == false)
            {
                Console.WriteLine("No such file");
                return;
            }
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
    7. Exit\n");
                string num = Console.ReadLine();
                string val = "";
                if (Int32.Parse(num) >= 1 && Int32.Parse(num) < 6)
                {
                    val = Console.ReadLine();
                }
                if (num == "1")
                {
                    ls.Search(val);
                }
                else if (num == "2")
                {
                    ;
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