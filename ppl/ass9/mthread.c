#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
// #include<windows.h>

// Structure for clock timer
typedef struct
{
    int sec;
    int min;
    int hrs;
} Clock;

// Increment hours
void *hrs_fun(void* arg) {
    Clock* nclock = arg;
    
    while (1)
    {
        sleep(60 * 60);
        nclock->hrs = nclock->hrs + 1;
        // printf("%d\n", new_clock->hours);
        nclock->min = 0;
        // new_clock->seconds = 0;
    }

}

// Increment minutes
void *min_fun(void* arg) {
    Clock* nclock = arg;
    
    while (1)
    {
        sleep(60);
        nclock->min = nclock->min + 1;
        // printf("%d\n", new_clock->minutes);
        nclock->sec = 0;
    }

}

// Increment Seconds
void *sec_fun(void* arg) {
    Clock* nclock = arg;
    
    while (1)
    {
        sleep(1);
        nclock->sec = nclock->sec + 1;
        // printf("%d\n", new_clock->seconds);
    }

}

void* print_fun(void* arg) {

    Clock* nclock = arg;

    char hours[3] = {'\0'};
    char minutes[3] = {'\0'};
    char seconds[3] = {'\0'};
    
    while (1)
    {
        if(nclock->hrs < 10) {
            sprintf(hours, "0%d", nclock->hrs);
        }else {
            sprintf(hours, "%d", nclock->hrs);
        }

        if(nclock->min < 10) {
            sprintf(minutes, "0%d", nclock->min);
        }else {
            sprintf(minutes, "%d", nclock->min);
        }

        if(nclock->sec < 10) {
            sprintf(seconds, "0%d", nclock->sec);
        }else {
            sprintf(seconds, "%d", nclock->sec);
        }
        
        printf("\r%s:%s:%s", hours, minutes, seconds);   
        //printf("%2d:%2d:%2d", nclock->hrs, nclock->min, nclock->sec);
    }
    
}



int main() {
    printf("Clock: \n");

    // Initializing object
    Clock* seconds = malloc(sizeof(Clock));
    seconds->sec = 0;
    seconds->hrs = 0;
    seconds->min = 0;


    // Thread objects
    pthread_t thread1, thread2, thread3, thread4;

    //Creating threads
    pthread_create(&thread1, NULL, sec_fun, seconds);
    pthread_create(&thread2, NULL, min_fun, seconds);
    pthread_create(&thread3, NULL, hrs_fun, seconds);
    pthread_create(&thread4, NULL, print_fun, seconds);

    //Joining threads
    int join1 = pthread_join(thread1, NULL);
    int join2 = pthread_join(thread2, NULL);
    int join3 = pthread_join(thread3, NULL);
    int join4 = pthread_join(thread3, NULL);

    

    printf("Clock ends!!\n");
}
