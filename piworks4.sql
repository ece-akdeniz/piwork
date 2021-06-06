with median_data as (
	select 
		country,
		avg(vac) as medianval
	from (
			select country,
			daily_vaccinations,
			row_number()
				over (
						partition by country
						order by date asc
					) as rowasc,
			row_number()
				over (
						partition by country
						order by date desc
					) as rowdesc
			from country_vaccination_stats
		)
	where rowasc in (rowdesc, rowdesc - 1, rowdesc + 1)
	group by 1
),

zero_checks as (
	select 
		country,
		sum(ISNULL(daily_vaccinations, 0)) as total
	from country_vaccination_stats
	group by 1

)

	select 
		rd.country as country,
		rd.date as date,
		ISNULL(rd.daily_vaccinations, 
				case 
					when zc.total = 0 then 0
					else md.medianval
			) as daily_vaccinations,
		rd.vaccines as vaccines
	from country_vaccination_stats as rd
	left join zero_checks zc on zc.country = rd.country
	left join median_data md on md.country = rd.country
