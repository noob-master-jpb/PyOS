#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* process_and_copy(const char *input) 
{
    size_t len = strlen(input);
    /*allocate len+1 to have room for '\0'*/
    char *out = malloc(len + 1);
    if (!out) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    size_t oi = 0;  // index into out[]
    for (size_t i = 0; i < len; ++i) {
        char c = input[i];
        if (c == '\n') {
            // if previous char '\n', skip this one
            if (oi > 0 && out[oi - 1] == '\n')
                continue;
        }
        out[oi++] = c;
    }
    out[oi] = '\0';  // null‑terminate
    return out;
}

int main(void) {
    char original[] = "Hello\n\n\nWorld!";
    char *modified = process_and_copy(original);

    printf("Original: %s\n", original);
    printf("Modified: \n%s\n", modified);

    free(modified);
    return 0;
}



