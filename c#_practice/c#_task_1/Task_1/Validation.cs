using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text;
using System.Globalization;
using System.Text.RegularExpressions;
using System.Threading.Tasks;


namespace Task_1
{
    public class Id
    {
        public static List<string> ids = new List<string>();
    }
    public class Input
    {
        public static bool ValidateInput(string val, string str)
        {
            Validation obj = new Validation(val);
            return obj.ValidateAll(str);
        }

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

        public static void ValidateFileInput(string file)
        {
            string[] lines = File.ReadAllLines(file);
            File.WriteAllText(file, string.Empty);
            foreach (string line in lines)
            {
                Validation v = new Validation(line);
                if (v.ValidateAll("add") == true)
                {
                    using (StreamWriter sw = File.AppendText(file))
                    {
                        sw.WriteLine(line);
                    }
                }
            }
        }
    }
    class Validation
    {
        String[] l = { };

        public Validation(string s)
        {
            this.l = s.Split(';');
        }
        public bool CheckLength()
        {
            try
            {
                if (l.Length != 7)
                {
                    throw new Exception("Wrong Length!");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }
            return true;
        }
        public bool CheckPeople()
        {
            var regexItem = new Regex("^[(a-zA-Z)' '(a-zA-Z)]*$");
            try
            {
                if (regexItem.IsMatch(l[5]) == false || regexItem.IsMatch(l[6]) == false)
                {
                    throw new Exception("Wrong Name!");
                }
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }
            return true;
        }
        public bool CheckUrl()
        {
            bool isUri = Uri.IsWellFormedUriString(l[4], UriKind.Absolute);
            try
            {
                if (isUri == false)
                {
                    throw new Exception("Wrong Url!");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }
            return true;
        }
        public bool CheckTime()
        {
            try
            {
                DateTime dt = DateTime.Parse(l[2]);
                DateTime dt1 = DateTime.Parse(l[3]);
                if (dt > dt1)
                {
                    throw new Exception("Time conflict!");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }
            return true;
        }
        public bool CheckDate()
        {
            try
            {
                DateTime dt = DateTime.Parse(l[1]);
                DateTime dt1 = DateTime.Now;
                if (dt < dt1)
                {
                    throw new Exception("Wrong date");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }
            return true;
        }
        public bool CheckId()
        {
            try
            {
                if (Id.ids.Contains(l[0]) || l[0].All(char.IsDigit) == false)
                {
                    throw new Exception("Wrong id!");
                }
                else if(Int32.Parse(l[0]) == 0)
                {
                    throw new Exception("Id can't be zero!");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }
            Id.ids.Add(l[0]);
            return true;
        }
        public bool ValidateAll(string str)
        {
            if (CheckLength() && CheckTime() && CheckPeople() && CheckDate() && CheckUrl())
            {
                if (str == "add")
                {
                    return CheckId();
                }
                return true;
            }
            if (Id.ids.Contains(l[0]))
            {
                Id.ids.Remove(l[0]);
            }
            return false;
        }
    }
}