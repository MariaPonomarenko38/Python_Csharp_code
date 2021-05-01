using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace MeetingOrder.Authentication
{
    public class TokenLogin
    {
        public string Id { get; set; }
        public string UserEmail { get; set; }
        public string Token { get; set; }
        public string TokenExpDate { get; set; }
    }
}