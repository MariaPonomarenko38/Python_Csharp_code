using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;

namespace MeetingOrder.Models
{
    public class OrderForm
    {
        [Required]
        public string MeetingId { get; set; }

    }
}
