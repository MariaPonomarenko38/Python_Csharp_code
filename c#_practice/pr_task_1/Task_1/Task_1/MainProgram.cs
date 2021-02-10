using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Task_1
{
    class MainProgram
    {
        static void Main(string[] args)
        {
            string s = "5;23.02.2021;13:23;15:50;httpstackoverflow.com;Karl Brown;Meggi Smith";
            Validation s1 = new Validation(s);
            s1.CheckUrl();
        }
    }
}
