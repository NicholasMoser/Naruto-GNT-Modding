#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

uint32_t RANDOM_SEED;
uint32_t* RANDOM_SEED_PTR = &RANDOM_SEED;

/*
Example seeds, retrieved via via asm opcode mftb:

dd80c261
ff4c7e21
06bfd461
0bd2e32b
10f04150
1603501a
1b165ee4
20296dae
253c7c78
2a4f8b42
2f629a0c
3475a8d6
*/

int32_t HSD_Randi(int32_t param_1)
{
  uint32_t uVar1;
  
  *(int32_t *)RANDOM_SEED_PTR = *(int32_t *)RANDOM_SEED_PTR * 0x343fd + 0x269ec3;
  uVar1 = param_1 * (*(uint32_t *)RANDOM_SEED_PTR >> 0x10);
  return ((int32_t)uVar1 >> 0x10) + (uint32_t)((int32_t)uVar1 < 0 && (uVar1 & 0xffff) != 0);
}

int main()
{
    // For current duplicate values in a row
    int dupe_in_row = 1;
	int last = -1;
	// Max duplicate values in a row
	int max_dupe_in_row = 1;
	int max_val = -1;
    
    int total_iterations = 1000000;
    int *array = (int *) malloc(0x29 * sizeof(int)); 
    RANDOM_SEED = 0x0e6ce3f2;
    for (int i = 0; i < total_iterations; i++) {
        uint32_t ind = HSD_Randi(0x29);
	    array[ind]++;

		// Check for duplicate values in a row
		if (ind == last) {
			dupe_in_row++;
			if (dupe_in_row > max_dupe_in_row) {
				max_dupe_in_row = dupe_in_row;
				max_val = last;
			}
		} else {
			// New value
			last = ind;
			dupe_in_row = 1;
		}
    }
    for (int i = 0; i < 0x29; i++) {
        printf("%02X -> %d\n", i, array[i]);
    }
    printf("Done with total %d\n", total_iterations);
    printf("Found %d in a row of value %d\n", max_dupe_in_row, max_val);

    return 0;
}
