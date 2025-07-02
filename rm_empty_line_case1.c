#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//ALL VARIABLES ARE DECLEARED HERE


char* process_and_copy(const char *input) 
{
    //ALL VARIABLES ARE DECLEARED HERE
    size_t length_of_input;
    char *out_put;
    size_t output_index = 0;  // index into out[]
    char temp;

    //length determination of input string 
    length_of_input = strlen(input);

    //allocate length+1 to have room for '\0' in the end
    out_put = malloc(length_of_input + 1);

    //format printing"Exit due to memory allocation failure"
    if (!out_put) 
    {   
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    //Appending Value to output array
    for (size_t i = 0; i <length_of_input; ++i) 
    {
        temp = input[i];
        if (temp == '\n') 
        {
            // if previous char '\n', skip this one
            if (output_index > 0 && out_put[output_index - 1] == '\n')
                continue;
        }
        out_put[output_index++] = temp;
    }
    // null‑terminate
    out_put[output_index] = '\0';  
    
    //Returning output to main as form of array
    return out_put;
}

int main(void) 
{
    char original[] = "Hello\n\n\nWorld!";
    char *modified = process_and_copy(original);

    printf("Original: %s\n", original);
    printf("Modified: \n%s\n", modified);

    free(modified);
    return 0;
}



