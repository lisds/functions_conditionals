test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          # rng = np.random.default_rng()
          # choices = np.arange(1, 11)
          # trials = rng.choice(choices, size=(10000, 1000))
          # scores = np.sum(trials, axis=1)
          # np.min(scores), np.max(scores)
          'code': r"""
          >>> 5090 <= total_score <= 5900
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
