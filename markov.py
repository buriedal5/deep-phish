import sys
import random

model = {}
strings = {}
strings_backwards = [] 
strings_pos = 0

def get_string(string):
    global strings_pos
    if strings.has_key(string):
        return strings[string]
    strings[string] = strings_pos
    strings_backwards.append(string)
    strings_pos += 1
    return strings_pos - 1

def add_to_model(prev_code, curr_code):
    if model.has_key((prev_code, curr_code)):
        model[(prev_code, curr_code)] += 1
    else:
        model[(prev_code, curr_code)] = 1

# helps with debugging
get_string("begin set 1")
get_string("begin set 2")
get_string("begin set 3")
get_string("begin set 4")
get_string("begin encore")
get_string("end set 1")
get_string("end set 2")
get_string("end set 3")
get_string("end set 4")
get_string("end encore")
get_string("end show")

for arg in sys.argv[1:]:
  fh = open(arg, "r")
  data = fh.readlines()
  prev_code = -1
  max_set = 0
  for line in data:
    curr_code = -1
    if line.startswith("http") or line.startswith("<"):
      curr_code = get_string(line)
      add_to_model(prev_code,curr_code)
    elif line.startswith("Set "):
      new_set = int(line[4:])
      max_set = new_set
      curr_code = get_string("begin set " + str(new_set))
      if (new_set > 1):
        end_set_code = get_string("end set " + str(new_set - 1))
        add_to_model(prev_code, end_set_code)
        add_to_model(end_set_code, curr_code)
    elif line.startswith("Encore"):
      curr_code = get_string("begin encore")
      if max_set > 0:
        end_set_code = get_string("end set " + str(max_set))
        add_to_model(prev_code, end_set_code)
        add_to_model(end_set_code, curr_code)
      max_set = 99
    elif len(line) > 2 and line[2] == "/":
      curr_code = -1
      if max_set == 99:
        add_to_model(prev_code,get_string("end encore"))
        add_to_model(get_string("end encore"),get_string("end show"))
      else:
        if max_set > 0:
          end_set_code = get_string("end set " + str(max_set))
          add_to_model(prev_code, end_set_code)
          add_to_model(end_set_code,get_string("end show"))
    prev_code = curr_code

  if max_set == 99:
    add_to_model(prev_code,get_string("end encore"))
    add_to_model(get_string("end encore"),get_string("end show"))
  else:
    if max_set > 0:
      end_set_code = get_string("end set " + str(max_set))
      add_to_model(prev_code, end_set_code)
      add_to_model(end_set_code,get_string("end show"))
  


intermediate = {}
for (key, value) in model.items():
    if intermediate.has_key(key[0]):
        tuple_list = intermediate[key[0]][0]
        tuple_list.append((key[1], value))
        value_sum = intermediate[key[0]][1]
        value_sum += value
        intermediate[key[0]] = (tuple_list, value_sum)
    else:
        intermediate[key[0]] = ([(key[1], value)], value)

final = {}
for (key, value) in intermediate.items():
    tuple_list = value[0]
    value_sum = value[1]
    for (code, count) in tuple_list:
        if not final.has_key(key):
            final[key] = {}
        final[key][code] = float(count)/float(value_sum)

begin_code = get_string("begin set 1")
end_code = get_string("end show")
curr_code = begin_code

print strings_backwards[77]

while curr_code != end_code:
    print strings_backwards[curr_code]
    probs = final[curr_code]
    rand = random.random()
    for (key, value) in probs.items():
        if (rand < value):
            curr_code = key
            break
        else:
            rand -= value
