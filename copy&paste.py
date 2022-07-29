# Text file
with open(f"{directory}/thconvsT.txt", "w") as my_txt_file:
    my_txt_file.write(f"")

import pickle

# Create pickle
my_empty_pickle_jar = open(f"path_to_save_location.pickle", "wb")
pickle.dump(object_to_pickle, my_empty_pickle_jar)
my_empty_pickle_jar.close()

# Open pickle
my_pickle_jar = open(f"path_to_pickle.pickle", "rb")
loaded_object = pickle.load(my_pickle_jar)
my_pickle_jar.close()

# Test skeleton
import unittest
import my_library


class TestFile(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(my_function, my_correct_answer)

        with self.assertRaises(ExpectedError):          # Context manager to check that error is thrown as expected
            my_library.my_function()


# Tkinter file selector
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
directory = filedialog.askopenfilename()


# Matplot lib skeleton
import matplotlib.pyplot as plt

plt.style.use('dark_background')
plt.rc('axes', axisbelow=True)

plt.figure()
for i in range(file_count):
    # fig, ax = plt.subplots()
    plt.scatter(temp[i],dens[i],c='red',s=0.5)
plt.ylabel(r'Density, $[g/cm^3]$',fontsize=18)
plt.xlabel('Temperature (°C)',fontsize=18)
# plt.ylim([0,100])
plt.yticks(fontsize=16, rotation=0)
plt.xticks(fontsize=16, rotation=0)
plt.grid()
plt.box(on=False)
plt.tight_layout()
plt.savefig(locstr+prefix+'rhovsT.tiff')
plt.show()


if __name__ == '__main__':
    unittest.main()
