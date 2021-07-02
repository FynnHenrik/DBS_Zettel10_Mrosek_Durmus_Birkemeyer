DB_NAME ="postgres"
DB_USER ="postgres"
DB_PASS ="D5gM24o8PQ49tl3c"
DB_HOST ="localhost"

import matplotlib.pyplot as plt
import matplotlib.widgets as mwidgets
import psycopg2

conn = psycopg2.connect(dbname=DB_NAME, user = DB_USER, password=DB_PASS,host=DB_HOST)

cur = conn.cursor()

#CO2 emissions
cur.execute("CREATE TABLE co2_emission(Entity Text, Code VARCHAR, Year int, \"Annual CO₂ emissions (tonnes )\" float);")
cur.execute("COPY co2_emission(Entity, Code, Year, \"Annual CO₂ emissions (tonnes )\") FROM '/home/arman/D/Datensatz1/co2_emission.csv' DELIMITER ',' CSV HEADER;")

#GDP 
cur.execute("CREATE TABLE gdp(\"Country Name\" VARCHAR PRIMARY KEY,\"Country Code\" VARCHAR, \"Indicator Name\" VARCHAR, \"Indicator Code\" VARCHAR, \"1960\" double precision, \"1961\" double precision, \"1962\" double precision, \"1963\" double precision, \"1964\" double precision, \"1965\" double precision, \"1966\" double precision, \"1967\" double precision, \"1968\" double precision,  \"1969\" double precision, \"1970\" double precision, \"1971\" double precision, \"1972\" double precision, \"1973\" double precision, \"1974\" double precision, \"1975\" double precision, \"1976\" double precision, \"1977\" double precision, \"1978\" double precision, \"1979\" double precision, \"1980\" double precision, \"1981\" double precision, \"1982\" double precision, \"1983\" double precision, \"1984\" double precision, \"1985\" double precision,  \"1986\" double precision, \"1987\" double precision, \"1988\" double precision, \"1989\" double precision, \"1990\" double precision,\"1991\" double precision,\"1992\" double precision,\"1993\" double precision,\"1994\" double precision,\"1995\" double precision,\"1996\" double precision,\"1997\" double precision,\"1998\" double precision,\"1999\" double precision,\"2000\" double precision,\"2001\" double precision,\"2002\" double precision,\"2003\" double precision,\"2004\" double precision,\"2005\" double precision,\"2006\" double precision,\"2007\" double precision,\"2008\" double precision,\"2009\" double precision,\"2010\" double precision,\"2011\" double precision, \"2012\" double precision,\"2013\" double precision,\"2014\" double precision, \"2015\" double precision,\"2016\" double precision,\"2017\" double precision, \"2018\" double precision, \"2019\" double precision, \"2020\" double precision);")
cur.execute("COPY gdp FROM '/home/arman/D/Datensatz1/gdp2.csv' WITH (format csv, header);");

#GDP countries only
cur.execute("CREATE TABLE gdpcountriesonly(\"Country Name\" VARCHAR PRIMARY KEY,\"Country Code\" VARCHAR, \"Indicator Name\" VARCHAR, \"Indicator Code\" VARCHAR, \"1960\" double precision, \"1961\" double precision, \"1962\" double precision, \"1963\" double precision, \"1964\" double precision, \"1965\" double precision, \"1966\" double precision, \"1967\" double precision, \"1968\" double precision,  \"1969\" double precision, \"1970\" double precision, \"1971\" double precision, \"1972\" double precision, \"1973\" double precision, \"1974\" double precision, \"1975\" double precision, \"1976\" double precision, \"1977\" double precision, \"1978\" double precision, \"1979\" double precision, \"1980\" double precision, \"1981\" double precision, \"1982\" double precision, \"1983\" double precision, \"1984\" double precision, \"1985\" double precision,  \"1986\" double precision, \"1987\" double precision, \"1988\" double precision, \"1989\" double precision, \"1990\" double precision,\"1991\" double precision,\"1992\" double precision,\"1993\" double precision,\"1994\" double precision,\"1995\" double precision,\"1996\" double precision,\"1997\" double precision,\"1998\" double precision,\"1999\" double precision,\"2000\" double precision,\"2001\" double precision,\"2002\" double precision,\"2003\" double precision,\"2004\" double precision,\"2005\" double precision,\"2006\" double precision,\"2007\" double precision,\"2008\" double precision,\"2009\" double precision,\"2010\" double precision,\"2011\" double precision, \"2012\" double precision,\"2013\" double precision,\"2014\" double precision, \"2015\" double precision,\"2016\" double precision,\"2017\" double precision, \"2018\" double precision, \"2019\" double precision, \"2020\" double precision);")
cur.execute("COPY gdpcountriesonly FROM '/home/arman/D/Datensatz1/gdpcountrysonly.csv' WITH (format csv, header);");

#Population Growth
cur.execute("CREATE TABLE population_growth(\"Country Name\" VARCHAR PRIMARY KEY,\"Country Code\" VARCHAR, \"Indicator Name\" VARCHAR, \"Indicator Code\" VARCHAR, \"1960\" VARCHAR, \"1961\" VARCHAR, \"1962\" VARCHAR, \"1963\"	VARCHAR, \"1964\" VARCHAR, \"1965\"	VARCHAR, \"1966\" VARCHAR, \"1967\"	VARCHAR, \"1968\" VARCHAR,  \"1969\" VARCHAR, \"1970\" VARCHAR, \"1971\" VARCHAR, \"1972\" VARCHAR, \"1973\" VARCHAR, \"1974\" VARCHAR, \"1975\" VARCHAR, \"1976\" VARCHAR, \"1977\" VARCHAR, \"1978\" VARCHAR, \"1979\" VARCHAR, \"1980\" VARCHAR, \"1981\" VARCHAR, \"1982\" VARCHAR, \"1983\" VARCHAR, \"1984\" VARCHAR, \"1985\" VARCHAR,  \"1986\" VARCHAR, \"1987\" VARCHAR, \"1988\" VARCHAR, \"1989\" VARCHAR, \"1990\" VARCHAR,\"1991\" VARCHAR,\"1992\" VARCHAR,\"1993\" VARCHAR,\"1994\" VARCHAR,\"1995\" VARCHAR,\"1996\" VARCHAR,\"1997\" VARCHAR,\"1998\" VARCHAR,\"1999\" VARCHAR,\"2000\" VARCHAR,\"2001\" VARCHAR,\"2002\" VARCHAR,\"2003\" VARCHAR,\"2004\" VARCHAR,\"2005\" VARCHAR,\"2006\" VARCHAR,\"2007\" VARCHAR,\"2008\" VARCHAR,\"2009\" VARCHAR,\"2010\" VARCHAR,\"2011\" VARCHAR, \"2012\" VARCHAR,\"2013\" VARCHAR,\"2014\" VARCHAR, \"2015\" VARCHAR,\"2016\" VARCHAR,\"2017\" VARCHAR, \"2018\" VARCHAR, \"2019\" VARCHAR, \"2020\" VARCHAR);")
cur.execute("COPY population_growth FROM '/home/arman/D/Datensatz1/population_growth.csv' WITH (format csv, header);");

#Population Growth Areas Only
cur.execute("CREATE TABLE population_growthareasonly(\"Country Name\" VARCHAR PRIMARY KEY,\"Country Code\" VARCHAR, \"Indicator Name\" VARCHAR, \"Indicator Code\" VARCHAR, \"1960\" VARCHAR, \"1961\" VARCHAR, \"1962\" VARCHAR, \"1963\"	VARCHAR, \"1964\" VARCHAR, \"1965\"	VARCHAR, \"1966\" VARCHAR, \"1967\"	VARCHAR, \"1968\" VARCHAR,  \"1969\" VARCHAR, \"1970\" VARCHAR, \"1971\" VARCHAR, \"1972\" VARCHAR, \"1973\" VARCHAR, \"1974\" VARCHAR, \"1975\" VARCHAR, \"1976\" VARCHAR, \"1977\" VARCHAR, \"1978\" VARCHAR, \"1979\" VARCHAR, \"1980\" VARCHAR, \"1981\" VARCHAR, \"1982\" VARCHAR, \"1983\" VARCHAR, \"1984\" VARCHAR, \"1985\" VARCHAR,  \"1986\" VARCHAR, \"1987\" VARCHAR, \"1988\" VARCHAR, \"1989\" VARCHAR, \"1990\" VARCHAR,\"1991\" VARCHAR,\"1992\" VARCHAR,\"1993\" VARCHAR,\"1994\" VARCHAR,\"1995\" VARCHAR,\"1996\" VARCHAR,\"1997\" VARCHAR,\"1998\" VARCHAR,\"1999\" VARCHAR,\"2000\" VARCHAR,\"2001\" VARCHAR,\"2002\" VARCHAR,\"2003\" VARCHAR,\"2004\" VARCHAR,\"2005\" VARCHAR,\"2006\" VARCHAR,\"2007\" VARCHAR,\"2008\" VARCHAR,\"2009\" VARCHAR,\"2010\" VARCHAR,\"2011\" VARCHAR, \"2012\" VARCHAR,\"2013\" VARCHAR,\"2014\" VARCHAR, \"2015\" VARCHAR,\"2016\" VARCHAR,\"2017\" VARCHAR, \"2018\" VARCHAR, \"2019\" VARCHAR, \"2020\" VARCHAR);")
cur.execute("COPY population_growthareasonly FROM '/home/arman/D/Datensatz1/population_growthareasonly.csv' WITH (format csv, header);")

#Population Total
cur.execute("CREATE TABLE population_total(\"Country Name\" Text, Year Int, Count Int);")
cur.execute("COPY population_total FROM '/home/arman/D/Datensatz1/population_total.csv' WITH (format csv, header);")

#World Cups
cur.execute("CREATE TABLE World_Cups(Year int PRIMARY KEY, Country Text, Winner Text, \"Runners-up\" Text, Third Text, GoalsScored int, QualifiedTeams int, MatchesPlayed int, Attendance VARCHAR);")
cur.execute("COPY World_Cups(Year, Country, Winner, \"Runners-up\", Third, GoalsScored, QualifiedTeams, MatchesPlayed, Attendance) FROM '/home/arman/D/FIFA World Cup/WorldCupsclean.csv' DELIMITER ',' CSV HEADER;")

#World Cup Matches
cur.execute("CREATE TABLE WorldCupMatches(Year int,	Datetime VARCHAR, Stage VARCHAR, \"Home Team Name\" VARCHAR, \"Home Team Goals\" VARCHAR, \"Away Team Goals\" VARCHAR, \"Away Team Name\" VARCHAR, \"Win conditions\" VARCHAR, \"Attendance\" VARCHAR, \"Half-time Home Goals\" VARCHAR,	\"Half-time Away Goals\" VARCHAR, \"RoundID\" VARCHAR, \"MatchID\" VARCHAR, \"Home Team Initials\" VARCHAR, \"Away Team Initials\" VARCHAR);")
cur.execute("COPY WorldCupMatches(Year,	Datetime, Stage, \"Home Team Name\", \"Home Team Goals\", \"Away Team Goals\", \"Away Team Name\", \"Win conditions\", \"Attendance\", \"Half-time Home Goals\",	\"Half-time Away Goals\", \"RoundID\", \"MatchID\", \"Home Team Initials\", \"Away Team Initials\") FROM '/home/arman/D/FIFA World Cup/WorldCupMatchesclean.csv' DELIMITER ',' CSV HEADER;")

#2018 Happiness
cur.execute("CREATE TABLE Happiness(\"Overall Rank\" SERIAL PRIMARY KEY, \"Country or Region\" TEXT, \"Score\" float, \"GDP per Capita\" float, \"Social Support\" float, \"Healthy Life Expectancy\" float, \"Freedom to make Life Choices\" float, \"Generosity\" float, \"Perceptions of Corruption\" VARCHAR);")
cur.execute("COPY Happiness FROM '/home/arman/D/happiness report (2015-2020)/2018.csv' WITH (format csv, header);");

#Countries which took Part in a WC
cur.execute("CREATE TABLE Countries(Name VARCHAR PRIMARY KEY, Appearances int);")
cur.execute("COPY Countries FROM '/home/arman/D/FIFA World Cup/wc_countries.csv' WITH (format csv, header);")

#GDP Areas Only
cur.execute("CREATE TABLE gdpareasonly(\"Country Name\" VARCHAR PRIMARY KEY,\"Country Code\" VARCHAR);")

#UNPIVOT Population Growth
cur.execute("CREATE TABLE PopGrowth AS (SELECT \"Country Name\" ,\"Country Code\", unnest(array[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]) AS Year, unnest(array[\"1960\" , \"1961\" , \"1962\" , \"1963\"	, \"1964\" , \"1965\"	, \"1966\" , \"1967\"	, \"1968\" ,  \"1969\" , \"1970\" , \"1971\" , \"1972\" , \"1973\" , \"1974\" , \"1975\", \"1976\", \"1977\", \"1978\", \"1979\", \"1980\", \"1981\", \"1982\", \"1983\", \"1984\", \"1985\",  \"1986\", \"1987\", \"1988\", \"1989\", \"1990\",\"1991\",\"1992\",\"1993\",\"1994\",\"1995\",\"1996\",\"1997\" ,\"1998\" ,\"1999\" ,\"2000\" ,\"2001\" ,\"2002\",\"2003\" ,\"2004\",\"2005\",\"2006\",\"2007\",\"2008\",\"2009\",\"2010\",\"2011\", \"2012\",\"2013\",\"2014\", \"2015\" ,\"2016\",\"2017\", \"2018\", \"2019\", \"2020\"]) AS popgrowth FROM population_growth);")

#UNPIVOT Population Growth Areas Only
cur.execute("CREATE TABLE PopGrowthAO AS (SELECT \"Country Name\" ,\"Country Code\", unnest(array[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]) AS Year, unnest(array[\"1960\" , \"1961\" , \"1962\" , \"1963\"	, \"1964\" , \"1965\"	, \"1966\" , \"1967\"	, \"1968\" ,  \"1969\" , \"1970\" , \"1971\" , \"1972\" , \"1973\" , \"1974\" , \"1975\", \"1976\", \"1977\", \"1978\", \"1979\", \"1980\", \"1981\", \"1982\", \"1983\", \"1984\", \"1985\",  \"1986\", \"1987\", \"1988\", \"1989\", \"1990\",\"1991\",\"1992\",\"1993\",\"1994\",\"1995\",\"1996\",\"1997\" ,\"1998\" ,\"1999\" ,\"2000\" ,\"2001\" ,\"2002\",\"2003\" ,\"2004\",\"2005\",\"2006\",\"2007\",\"2008\",\"2009\",\"2010\",\"2011\", \"2012\",\"2013\",\"2014\", \"2015\" ,\"2016\",\"2017\", \"2018\", \"2019\", \"2020\"]) AS popgrowth FROM population_growthareasonly);")

#UNPivot GDP
cur.execute("CREATE TABLE GdpNew AS (SELECT \"Country Name\" ,\"Country Code\", unnest(array[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]) AS Year, unnest(array[\"1960\" , \"1961\" , \"1962\" , \"1963\"	, \"1964\" , \"1965\"	, \"1966\" , \"1967\"	, \"1968\" ,  \"1969\" , \"1970\" , \"1971\" , \"1972\" , \"1973\" , \"1974\" , \"1975\", \"1976\", \"1977\", \"1978\", \"1979\", \"1980\", \"1981\", \"1982\", \"1983\", \"1984\", \"1985\",  \"1986\", \"1987\", \"1988\", \"1989\", \"1990\",\"1991\",\"1992\",\"1993\",\"1994\",\"1995\",\"1996\",\"1997\" ,\"1998\" ,\"1999\" ,\"2000\" ,\"2001\" ,\"2002\",\"2003\" ,\"2004\",\"2005\",\"2006\",\"2007\",\"2008\",\"2009\",\"2010\",\"2011\", \"2012\",\"2013\",\"2014\", \"2015\" ,\"2016\",\"2017\", \"2018\", \"2019\", \"2020\"]) AS gdp FROM gdp);")

#CREATE OUR DB FROM MODEL
cur.execute("CREATE TABLE Land AS SELECT DISTINCT \"Country Name\" AS Name, \"Country Code\" AS Id FROM population_growth;")

cur.execute("CREATE TABLE DatenOfLand AS SELECT P.\"Country Name\" AS Name, P.\"Country Code\" AS Id, P.Year AS Year, \"Overall Rank\" AS \"Happiness Rank\", G.\"gdp\" , \"Score\" AS \"Happiness Score\", Count AS PopTotal, \"Annual CO₂ emissions (tonnes )\" AS \"Co2/Jahr\" FROM PopGrowth P, GdpNew G, (SELECT \"Overall Rank\",\"Score\",\"Country or Region\" FROM Happiness) H, co2_emission E, population_total T WHERE P.\"Country Name\" = H.\"Country or Region\" AND H.\"Country or Region\" = E.Entity AND P.Year = E.Year AND E.Entity = T.\"Country Name\" AND E.Year = T.Year AND G.\"Country Name\" = T.\"Country Name\" AND G.Year = T.Year;")

cur.execute("CREATE TABLE Area AS (SELECT DISTINCT \"Country Name\" AS Name, \"Country Code\" AS Id FROM population_growthareasonly);") 

cur.execute("CREATE TABLE GdpAreas AS (SELECT \"Country Name\" ,\"Country Code\", unnest(array[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]) AS Year, unnest(array[\"1960\" , \"1961\" , \"1962\" , \"1963\"	, \"1964\" , \"1965\"	, \"1966\" , \"1967\"	, \"1968\" ,  \"1969\" , \"1970\" , \"1971\" , \"1972\" , \"1973\" , \"1974\" , \"1975\", \"1976\", \"1977\", \"1978\", \"1979\", \"1980\", \"1981\", \"1982\", \"1983\", \"1984\", \"1985\",  \"1986\", \"1987\", \"1988\", \"1989\", \"1990\",\"1991\",\"1992\",\"1993\",\"1994\",\"1995\",\"1996\",\"1997\" ,\"1998\" ,\"1999\" ,\"2000\" ,\"2001\" ,\"2002\",\"2003\" ,\"2004\",\"2005\",\"2006\",\"2007\",\"2008\",\"2009\",\"2010\",\"2011\", \"2012\",\"2013\",\"2014\", \"2015\" ,\"2016\",\"2017\", \"2018\", \"2019\", \"2020\"]) AS gdp FROM gdp NATURAL JOIN Area);")

cur.execute("CREATE TABLE DatenOfArea AS SELECT P.\"Country Name\" AS Name, P.\"Country Code\" AS Id, P.Year AS Year, G.\"gdp\", \"Annual CO₂ emissions (tonnes )\" AS \"Co2/Jahr\" FROM PopGrowthAO P, GdpAreas G, (SELECT * FROM co2_emission NATURAL JOIN Area) E WHERE P.\"Country Name\" = E.Entity AND P.Year = E.Year AND E.Entity = G.\"Country Name\" AND E.Year = G.Year;")

cur.execute("CREATE TABLE FifaWorldCup AS SELECT Year, Country AS Name, Winner AS First, \"Runners-up\" AS Second, Third, GoalsScored FROM World_Cups;")
#END DB MODEL

#GET AVG GDP OF LANDS OVER YEARS
cur.execute("CREATE TABLE avg_gdp AS (SELECT Name , AVG(G.gdp/CAST(G.PopTotal AS double precision)) AS AVGDP FROM DatenOfLand G WHERE G.gdp IS NOT NULL AND G.PopTotal IS NOT NULL GROUP BY Name);")
#Table of Country, Podium Finishes, AVG GDP
cur.execute("SELECT C.Name, COUNT(C.Name), AVGDP  FROM FifaWorldCup F, (Land NATURAL JOIN avg_gdp) AS C WHERE F.First = C.Name OR F.Second = C.Name OR F.Third = C.Name GROUP BY C.Name, AVGDP ORDER BY COUNT(C.Name) DESC;")
table_1 = cur.fetchall()
cur.execute("SELECT AVG(G.gdp/CAST(G.PopTotal AS double precision)) FROM DatenOfLand G WHERE G.gdp IS NOT NULL AND G.PopTotal IS NOT NULL;")
avg = cur.fetchall()
cur.execute("SELECT AVG(G.gdp/CAST(G.PopTotal AS double precision)) FROM (DatenOfLand NATURAL JOIN Countries) G WHERE G.gdp IS NOT NULL AND G.PopTotal IS NOT NULL;")
wc_avg = cur.fetchall()
table_1.insert(0,("Average", None, avg[0][0]))
table_1.insert(1,("WC_AVG", None, wc_avg[0][0]))
print(table_1)
colors = ['k','y']
for i in range(2,len(table_1)):
    if (table_1[i][2]>table_1[0][2]) & (table_1[i][2]>table_1[1][2]):
        colors.append('b')
    elif table_1[i][2]<table_1[0][2]:
        colors.append('r')
    else:
        colors.append('g')
plt.bar([table_1[i][0] for i in range(len(table_1))],[table_1[i][2] for i in range(len(table_1))],color = colors)
plt.xticks(rotation = -20)
plt.title("Average GDP per capita of Countries successful in Fifa World Cups")
plt.ylabel('Average GDP of Country')
plt.xlabel('Countries by # of podium finishes in descending order')
plt.show()

#cur.execute("SELECT Name, First, Second, Third FROM FifaWorldCup WHERE Year = \'2018\';")
#print(cur.fetchall())
#cur.execute("SELECT DISTINCT Year FROM DatenOfLand ORDER BY Year")
#print(cur.fetchall())
#cur.execute("SELECT L.Name, CASE WHEN L.Name = F.Name THEN F.Name WHEN L.Name =  First THEN FIRST WHEN L.Name = Second THEN Second ELSE Third END AS COL, gdp, \"Happiness Rank\", \"Happiness Score\", PopTotal  FROM (SELECT Name, First, Second, Third FROM FifaWorldCup WHERE Year = \'2018\') F, (SELECT Name, gdp, \"Happiness Rank\", \"Happiness Score\", PopTotal FROM DatenOfLand WHERE Year = \'2018\') L WHERE L.Name = First OR L.Name = Second OR L.Name = Third OR L.Name = F.Name;")
#table_2018 = cur.fetchall()
#print(table_2018)

cur.close()

conn.close()
