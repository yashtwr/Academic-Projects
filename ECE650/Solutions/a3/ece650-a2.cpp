// Compile with c++ ece650-a2cpp -std=c++11 -o ece650-a2
#include <iostream>
#include <sstream>
#include <vector>
#include<queue>
using namespace std;

void BFS(vector <vector<int>>nums,int s,int d)
{   int p_array[nums.size()];
    int d_array[nums.size()];
    char colour[nums.size()];
    queue<int> q;
    for (int i = 0;i<nums.size();i++)
    {
        p_array[i] = -1;
        d_array[i] = -1;
        colour[i] = 'w';

    }
    colour[s] = 'g';
    d_array[s] = 0;
    q.push(s);
    while(!q.empty())
    {
        int u = q.front();
        q.pop();
        for (int j = 0;j<nums[u].size();j++)
        {
            int v = nums[u][j];
            if(colour[v]=='w')
            {
                colour[v] = 'g';
                d_array[v] = d_array[u]+1 ;
                p_array[v] = u;
                q.push(v);
            }

        }
        colour[u] = 'b';
    }
    if(colour[d] == 'w')
    {
        cerr << "Error: Shortest path doesnot exist" <<'\n';
    }
    else
    {
        int temp = d;
        vector <int> path;
        while(temp != s)
        {
            path.push_back(temp+1);
            temp = p_array[temp];
        }
        path.push_back(s+1);
        for (int i = path.size()-1;i>=1;i--)
        {
            cout << path[i] <<'-';
        }
        cout << path[0] <<'\n';
    }

}
void print_list(vector <vector<int>> nums)
{
     for (int i=0;i<nums.size();i++)
            {
                if(nums[i].size() == 0)
                {
                    cout << "Vertex "<< i+1 << "-->[ ]";
                }
                else
                {   cout << "Vertex " << i+1 << "-->[";
                    for(int a : nums[i]){
                        cout << a+1 <<',';}
                    cout << ']';
                }
            }
}
int create_adjacencylist (std::vector<std::vector<int>> & nums,string temp)
{
    int i = 0;
    while(i< temp.length() - 1)
    {
        i = temp.find('<',i);
        int j = temp.find ('>',i);
        int k = temp.find(',',i);
        int a = std::stoi(temp.substr(i+1,k-i-1));
        int b = std::stoi(temp.substr(k+1,j-k-1));
        i = j+1;
        if(a<=0 || b<=0 || a>nums.size() || b >nums.size())
        {
            return -1;
        }
        else
        {   nums[a-1].push_back(b-1);
            nums[b-1].push_back(a-1);
        }
    }
    return 0;

}

int main()
 {
    std::vector<std::vector<int>> nums;
    while (!std::cin.eof()) {
        // print a promt

        // read a line of input until EOL and store in a string
        std::string line;
        std::getline(std::cin, line);
        std::istringstream input(line);
        string temp;
        while(!input.eof())
        {
            input >> temp;
            cout <<temp << ' ';
            if (temp[0]=='V')
                {
                    int length;
                    input >> length;
                    if(length > 0)
                    {
                        nums.clear();
                        nums.resize(length);
                        cout << nums.size();
                    }
                    else
                    {
                        cerr << "Error: There should be atleast one vertex"<< '\n';
                        break;
                    }
                }// End for vertex
            if (temp[0] == 'E')
            {
                 if(nums.size() == 0)
                        {
                            cerr << "Error: Please Enter the number of vertices first" << '\n';
                            break;
                        }
                input >> temp;
                cout << temp;
                int result = create_adjacencylist(nums,temp);
                if(result == -1)
                {
                    cerr << "Error: Please enter the correct edges" << '\n';
                    break;
                }

            }
            if(temp[0] == 's')
            {
                int source,destination;
                input >> source;
                input >> destination;
                if(source <=0 || destination <=0 || source >nums.size() || destination >nums.size())
                {
                    cerr << "Error: Please enter correct source and destination values" << '\n';
                }
                else{
                    BFS(nums,source-1,destination-1);
                }
            }



        }
    }
return 0;

}
