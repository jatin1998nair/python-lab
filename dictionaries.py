# for using dictionaries  and its functions
#create a dictionary example iphone  releases
released ={
	"iphone":2007,
	"iphone 3G":2008,
	"iphone 3GS":2009,
	"iphone 4":2010,
	"iphone 4S":2011,
	"iphone 5":2012,
	}
print(released)
released.values()
released.items()
released1 ={
	"iphone 5S":2013}
released.update(released1)
released.items()
released2 = released.copy()
print (released2)
released3 ={"iphone 6":2014}
released.fromkeys(released, released2)
released.get("iphone 5S")
released.pop("iphone")
print(released)
released.popitem()
print(released)
released.clear()
