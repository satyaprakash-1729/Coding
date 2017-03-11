#include <iostream>
#include <algorithm>
#include <limits.h>

using namespace std;

bool comp(int a, int b){
    return a>b;
}

int maxMoriarty(char a[], char b[], bool done[], int n, int doneIndex){
    if(n==1){
        char temp;
        for(int i=0;i<n;i++){
            if(!done[i]){
                temp = b[i];
                done[i]=1;
                break;
            }
        }
        return (a[0]>=temp)?0:1;
    }
    if(doneIndex!=-1)
        done[doneIndex]=1;
    int maxa=INT_MIN;
    int temp2;
    int index = 0;
    for(int i=0;i<n;i++){
        if(!done[i]){
            if((temp2 = (((b[i]>a[n-1])?1:0) + maxMoriarty(a,b,done,n-1,i))) > maxa){
                done[index]=0;
                maxa = temp2;
                index = i;
            }
        }
    }
    return maxa;
}

int main(int argc, char const *argv[])
{
    int n;
    cin>>n;
    char a[n];
    char b[n];
    bool done[n] = {0};
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=0;i<n;i++){
        cin>>b[i];
    }
    sort(a,a+n);
    sort(b,b+n);
    int c = 0;
    int c2;
    for(int i=0;i<n;i++){
        if(a[i]>b[i]){
            c++;
        }
    }
    c2 = maxMoriarty(a,b,done,n,-1);
    cout<<c<<endl<<c2<<endl;
    return 0;
}