using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WebApplication1.Models
{
	public class OwnerParameters
	{
		public int PageNumber { get; set; } = 1;

		private int _pageSize;
		private string _sort_by = "Owner";
		private string _sort_type = "asc";
		private string _search;
		public int PageSize
		{
			get { return _pageSize; }
			set { _pageSize = value; }
		}
		public string Sort_by
		{
			get { return _sort_by; }
			set { _sort_by = value; }
		}
		public string Sort_type
		{
			get { return _sort_type; }
			set { _sort_type = value; }
		}
		public string Search
		{
			get { return _search; }
			set { _search = value; }
		}
	}
}
