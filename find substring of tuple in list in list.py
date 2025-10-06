
def query_list():
  new_query_list = ['the title', 'Megabug-07-21-25-028', 'Megabug-07-21-25-013', 'Megabug-07-21-25-009', 'Megabug-07-21-25-018', 'Megabug-TEST3 7/21', 'Megabug-CSCwi84995', 'Megabug Test Case 4.23.2025', 'Megabug-TEST5 7/21', 'Megabug-TEST5 7/21', 'Megabug-07-21-25-007', 'Megabug-CSCwj54321', 'Megabug-TEST7 7/21', 'Megabug-07-21-25-023', 'Megabug-07-21-25-003', 'Megabug-CSCwi84985', 'Megabug-07-21-25-015', 'the title', 'Megabug-CSCwi84995', 'Megabug-07-21-25-007', 'the title', 'the title', 'the title', 'Megabug-07-21-25-010', 'Megabug-07-21-25-027', 'the title', 'Megabug-TEST3 7/21', 'Megabug-07-11-25-004', 'Megabug-CSCwi84967', 'Megabug-TEST5 7/21', 'Megabug-07-09-25-002', 'Megabug Test Case', 'the title', 'Megabug-07-21-25-006', 'Megabug-07-21-25-017', 'Megabug-CSCwi84967', 'Megabug-CSCwi84999', 'Megabug-CSCwm77551', 'Megabug-07-21-25-002', 'Megabug-TEST 7/21', 'Megabug-TEST4 7/21', 'Megabug-CSCwi84967', 'Megabug-CSCwi84988', 'Megabug Test Case', 'Megabug-07-21-25-007', 'Megabug-TEST5 7/21', 'Megabug-CSCwi84975', 'Megabug-07-21-25-019', 'Megabug Test Case 4.23.2025', 'Megabug-07-21-25-008', 'Megabug-TEST2 7/21', 'Megabug Test Case 4.23.2025', 'Megabug-07-21-25-020', 'Megabug-07-21-25-024', 'Megabug-07-11-25-002', 'Megabug-07-21-25-016', 'Megabug-07-21-25-025', 'Megabug Test Case 4.23.2025', 'Megabug-07-09-25-001', 'Megabug-TEST5 7/21', 'Megabug-07-21-25-004', 'Megabug-TEST 7/21', 'Megabug-07-21-25-021', 'Megabug-TEST5 7/21', 'the title', 'Megabug-TEST2 7/21', 'Megabug-CSCwi84967', 'Megabug-07-21-25-014', 'Megabug-07-21-25-007', 'Megabug-07-21-25-005', 'Megabug Test Case 6.26.2025-1', 'Megabug-TEST4 7/21', 'Megabug-07-21-25-012', 'the title', 'Megabug-TEST8 7/21', 'Megabug-07-21-25-022', 'Megabug-TEST3 7/21', 'Megabug Test Case 4.23.2025', 'Megabug-TEST5 7/21', 'Megabug-07-11-25-001', 'Megabug-07-21-25-026', 'Megabug-07-21-25-011', 'Megabug-07-21-25-001', 'Megabug-07-11-25-003', 'Megabug-07-21-25-007', 'the title']
  return new_query_list

megabug_lst = [('CSCwi84967', 'catastrophic','megabug', 'FPRMID3, FPRMID3, FPRMID, FSIGHT, FPRLOW, FPRLOW, FPRLOW, FPRMID3',22,5), ('CSCwi84975', 'catastrophic','megabugu', 'CBR8',22,5), ('CSCwixxxx', 'catastrophic','megabugu', 'CBR8',22,5)] 


def create_substring():
  substring = []
  for tup in megabug_lst:
      tupl = tup[0]
      substring.append(tupl)
  return substring


def queries_matching_substring():
  found_items = [
      item for item in query_list() 
      if any(sub in item for sub in create_substring())
  ]
  return found_items


def substring_not_in_query():
  items_not_found_as_substring = []
  for item in create_substring():
      found_as_substring = False
      for s in queries_matching_substring():
          if item in s:
              found_as_substring = True
              break  # Found the item as a substring, no need to check further strings
      if not found_as_substring:
          items_not_found_as_substring.append(item)
  return items_not_found_as_substring


def create_new_megabug_list():
  found_tuples = [
      tup for tup in megabug_lst
      if any(
          sub in element
          for element in tup
          for sub in substring_not_in_query()
          if isinstance(element, str) # Ensure element is a string before checking for substring
      )
  ]

  return found_tuples



new_mega_list = create_new_megabug_list()
print()
print('new_mega_list')
print(new_mega_list)
print()