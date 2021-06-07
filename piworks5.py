import pandas as pd

data = {"Device_Type": ["AXO145", "TRU151", "ZOD231", "YRT326", "LWR245"],
	"Stats_Access_Link": ["<url>https://xcd32112.smart_meter.com</url>",
				"<url>http://txh67.dia_meter.com</url>",
				"<url>http://yT5495.smart_meter.com</url>",
				"<url>https://ret323_TRu.crown.com</url>",
				"<url>https://luwr3243. celcius. com</url>"]}

df = pd.DataFrame(data)
df["Stats_Access_Link"] = df["Stats_Access_Link"].apply(lambda x: x[13:-6])
print(df)
