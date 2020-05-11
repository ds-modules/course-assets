test = {
	"name": "q11",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> np.count_nonzero(hispanic_and_white_data[0] == hispanic_and_white) == 15114
					True
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