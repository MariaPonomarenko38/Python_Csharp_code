using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Reflection;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace Task_2
{
    public class Input
    {
        public static string ValidateFileName()
        {
            while (true)
            {
                Console.WriteLine("Write file name:");
                string val = Console.ReadLine();
                try
                {
                    if (File.Exists(val) == false)
                    {
                        throw new Exception("File doensn't exist");
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                    continue;
                }
                return val;
            }
        }
    }
    public class Validate
    { 
        public static DateTime TimeConflict(DateTime a, DateTime b)
        {
            if (a > b)
            {
                Console.WriteLine("We have time conflict");
                throw new Exception();
            }
            else
            {
                return b;
            }
        }
        public static string CheckPerson(string val)
        {
            var regexItem = new Regex("^[(a-zA-Z)' '(a-zA-Z)]*$");
            if (regexItem.IsMatch(val) == false)
            {
                Console.WriteLine("Wrong name");
                throw new Exception();
            }
            else
            {
                return val;
            }
        }
        public static string CheckUrl(string val)
        {
            if (Uri.IsWellFormedUriString(val, UriKind.Absolute) == false)
            {
                Console.WriteLine("Wrong URL");
                throw new Exception();
            }
            else
            {
                return val;
            }
        }
        public static string CheckDate(string val)
        {
            DateTime dt = DateTime.Parse(val);
            DateTime dt1 = DateTime.Now;
            if (dt < dt1)
            {
                Console.WriteLine("Date conflict");
                throw new Exception();
            }
            else
            {
                return val;
            }
        }
        //public static string CheckId(string val)
        //{
        //    if (val.All(char.IsDigit) == false)
        //    {
        //        Console.WriteLine("Id is wrong");
        //        throw new Exception();
        //    }
        //    else
        //    {
        //        return val;
        //    }
        //}
    }
}
