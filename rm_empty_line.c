//CASE 1 Implementation //
#include <stdio.h>
#include <string.h>
char* rm_empty_lin(char *arr)
{
    //Size of Array Calculation
    int size = (sizeof(arr)/sizeof(arr[0]));
    //Special char in array calculation
    int i,count=0;
    char temp[]= arr;
    for(i=0;i<size;i++)
    {
        if(temp[i]==ascii(("\n")))
        {
            count++;
        }
    }
    //Output array declearation
    char*out_arr[(size-(count-1))];
    //Appending Value in "out_arr" after removal of blank space
    int map=0;
    int temp1=0;
    for(i=0;i<z;i++)
    {
        if(temp[i]=="\n")
        {
            if(temp[i+1]!="\n")
            {
                out_arr[(i-temp1)]="\n";
            }
            map=i;
            temp1++;
        }
        else if((map+1)==i)
        {
            out_arr[i-(count-1)]=temp[i];
        }
        else
        {
            out_arr[i]=temp[i];
        }
    }
    return out_arr;


}




int main()
{
    char text[]="Hello\n\n\nWorld!";
    char *my_arr=rm_empty_lin(text);
    int size=(sizeof(my_arr)/sizeof(my_arr[0]));
    int i;
    for(i=0;i<size;i++)
    {
        printf("%c",my_arr[i]);
    }
    printf("\n");
    return 0;
}