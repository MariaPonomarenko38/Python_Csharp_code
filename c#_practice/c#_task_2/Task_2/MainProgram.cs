using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace Task_2
{
    class MainProgram
    {
        public static class FillCollection<T> where T : MobileNumber, new()
        {
            public static Collection<T> Method(string file) 
            {
                Collection<T> a = new Collection<T>();
                string[] lines = File.ReadAllLines(file);
                File.WriteAllText(file, string.Empty);
                foreach (string line in lines)
                {
                    using (StreamWriter sw = File.AppendText(file))
                    {
                        sw.WriteLine(line);
                        var instance = Activator.CreateInstance<T>();
                        try
                        {
                            instance = Activator.CreateInstance(typeof(T), new object[] { line }) as T;
                        }
                        catch //(System.Reflection.TargetInvocationException)
                        {
                            //Console.WriteLine(e.InnerException.Message);
                            Console.WriteLine("Wrong format of some values!");
                            continue;
                        }
                        Console.WriteLine(instance);
                        a.AddTo(instance, "None");
                    }   
                }
                a.RewriteFile(file);
                return a;
            }
        }
        static void Main(string[] args)
        {
            //try
            //{
            //    MobileNumber a = new MobileNumber("6;Kateryna;Korniienko;+38055250;5056;56304892;5000.50;2010-03-09;");
            //}
            //catch
            //{
            //    Console.WriteLine("OPPS");
            //}
            ////Console.WriteLine(a);
            string file_name = Input.ValidateFileName();
            Collection<MobileNumber> ls = FillCollection<MobileNumber>.Method(file_name);
            //Collection<MobileNumber> ls = new Collection<MobileNumber>();
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
                if (num.All(char.IsDigit) == false)
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
                    MobileNumber obj = new MobileNumber();
                    try
                    {
                        obj = new MobileNumber(val);
                    }
                    catch 
                    {
                        Console.WriteLine("Rewrite values!");
                        continue;
                    }
                    ls.AddTo(obj, file_name);
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
