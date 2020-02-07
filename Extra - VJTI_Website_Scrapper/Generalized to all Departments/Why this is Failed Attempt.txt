Failed Attempt :
	 I was trying to generalize web scraping to all departments, but they all don't have common semantics.
	 So for each department one will have to write different scrapper as each department page have a different structure.
	 for example 
	 Order of columns in table: Designation is first in civil while the name is first in comp
	 There is no column for a photo in comp
	 Specialisation in electrical is written as Specialization in civil and [MS]Specialization in comp
	 Extension in Civil and Electrical is written as Phone in Comp
	 We can solve this naming conflict by hard-coding but there are conflicts in the structure of HTML too
	 Content in <span> in civil while in <p> for electrical.
	 and many more...