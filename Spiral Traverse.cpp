using namespace std;

vector<int> spiralTraverse(vector<vector<int>> array) {
 int T,B,L,R,dir;
    T=0;
    B=array.size()-1;
    L=0;
    R=array[0].size()-1;
    dir=0;
    int i;
    vector<int> ans;
    
    while(T<=B && L<=R)
    {
        if(dir==0)
        {
            for(i=L;i<=R;i++)
                ans.push_back(array[T][i]);
            T++;
        }
        else if(dir==1)
        {
            for(i=T;i<=B;i++)
                ans.push_back(array[i][R]);
            R--;
        }
        else if(dir==2)
        {
            for(i=R;i>=L;i--)
                ans.push_back(array[B][i]);
            B--;
        }
        else if(dir==3)
        {
            for(i=B;i>=T;i--)
                ans.push_back(array[i][L]);
            L++;
        }
        dir=(dir+1)%4;
    }
    return ans;
}
