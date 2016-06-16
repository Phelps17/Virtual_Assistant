import time
import datetime

class DateTime :
	def get_date(self) :
		return time.strftime("%A, %B %d, %Y")

	def get_time(self) :
		return time.strftime("%I:%M %p")

	def get_day(self) :
		return time.strftime("%d")

	def get_day_string(self) :
		return time.strftime("%A")

	def get_month(self) :
		return time.strftime("%m")

	def get_month_string(self) :
		return time.strftime("%B")

	def get_year(self) :
		return time.strftime("%Y")

	def get_hour(self) :
		return time.strftime("%I")

	def get_minute(self) :
		return time.strftime("%M")

	def get_am_pm(self) :
		return time.strftime("%p")

	def get_timezone(self) :
		return time.strftime("%Z")

	def time_to(self, other_time_string) :
		format_other_time_string = self.get_year()+"-"+self.get_month()+"-"+self.get_day()+" "+other_time_string
		other_time = datetime.datetime.strptime(format_other_time_string, "%Y-%m-%d %I %M %p")

		#convert to unix timestamp
		now_ts = time.mktime(datetime.datetime.now().timetuple())
		ot_ts = time.mktime(other_time.timetuple())

		#calculate the difference
		dif_secs = int(ot_ts-now_ts)

		if (dif_secs >= 0) :
			dif_hours = dif_secs/60/60
			dif_secs = dif_secs - (3600*dif_hours)
			dif_min = dif_secs/60
			return str(dif_hours)+" hours and "+str(dif_min)+" minutes until "+other_time_string+"."
		else :
			dif_secs = abs(dif_secs)
			dif_hours = dif_secs/60/60
			dif_secs = dif_secs - (3600*dif_hours)
			dif_min = dif_secs/60
			return str(dif_hours)+" hours and "+str(dif_min)+" minutes since "+other_time_string+"."

	def days_to(self, other_day) :
		pass

now = DateTime()
print now.get_date()
print now.get_time()
print now.get_day()
print now.get_day_string()
print now.get_month()
print now.get_month_string()
print now.get_year()
print now.get_hour()
print now.get_minute()
print now.get_am_pm()
print now.get_timezone()
print now.time_to("1 00 AM")
print now.time_to("5 00 AM")
