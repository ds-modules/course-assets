test = {
	"name": "q10",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> list(np.isclose([avg_pop_hispanic, avg_pop_white], [20, 10], atol = 5))
					[True, True]
					""",
					"hidden": True,
					"locked": True,
				}, 
			],
			"scored": False,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}, 
	]
}