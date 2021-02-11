using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text;
using System.Globalization;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

public class LengthException : Exception
{
    public LengthException(string message)
        : base(message)
    { }
}
public class NameException : Exception
{
    public NameException(string message)
        : base(message)
    { }
}
public class TimeException : Exception
{
    public TimeException(string message)
        : base(message)
    { }
}

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

        public static bool ValidateFileName(string val)
        {
            return File.Exists(val);
        }

        public static void ValidateFileInput(string file)
        {
            string[] lines = File.ReadAllLines(file);
            File.WriteAllText(file, string.Empty);
            // Display the file contents by using a foreach loo

            foreach (string line in lines)
            {
                // Use a tab to indent each line of the file.
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
                    throw new LengthException("Wrong Length!");
                }
            }
            catch (LengthException)
            {
                Console.WriteLine("Wrong Length");
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
                    throw new NameException("Wrong Name!");
                }
            }
            catch (NameException)
            {
                Console.WriteLine("Wrong Name!");
                return false;
            }
            return true;
        }
        public bool CheckUrl()
        {
            bool isUri = Uri.IsWellFormedUriString(l[4], UriKind.RelativeOrAbsolute);
            try
            {
                if (isUri == false)
                {
                    throw new Exception();
                }
            }
            catch
            {
                Console.WriteLine("Wrong Url!");
                return false;
            }
            return true;
        }
        public bool CheckTime()
        {
            var regexItem = new Regex("^(?:0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$");
            try
            {
                if (regexItem.IsMatch(l[2]) == false || regexItem.IsMatch(l[3]) == false)
                {
                    throw new NameException("Wrong Time!");
                }
            }
            catch (NameException)
            {
                Console.WriteLine("Wrong Time!");
                return false;
            }
            return true;
        }
        public bool CheckDate()
        {
            try
            {
                DateTime dt = DateTime.Parse(l[1]);
                if (dt.Year < 2021)
                {
                    throw new Exception();
                }
            }
            catch
            {
                Console.WriteLine("Wrong Date!");
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
                    throw new Exception();
                }
            }
            catch
            {
                Console.WriteLine("Wrong Id!");
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