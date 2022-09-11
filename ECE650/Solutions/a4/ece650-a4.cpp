// Compile with c++ ece650-a2cpp -std=c++11 -o ece650-a2
#include <iostream>
#include <sstream>
#include <vector>
#include<algorithm>
#include <memory>
// defines Var and Lit
#include "minisat/core/SolverTypes.h"
// defines Solver
#include "minisat/core/Solver.h"
using namespace std;



int create_adjacencylist (std::vector<std::vector<int>> & nums,string temp)
{
    int i = 0;
    while(i< (int)temp.length() - 1)
    {
        i = temp.find('<',i);
        int j = temp.find ('>',i);
        int k = temp.find(',',i);
        int a = std::stoi(temp.substr(i+1,k-i-1));
        int b = std::stoi(temp.substr(k+1,j-k-1));
        i = j+1;
        if(a<=0 || b<=0 || a>(int)nums.size() || b >(int)nums.size())
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
vector <vector<int>> create_edges(vector <vector<int>> nums)
{   
    vector <vector<int>> temp;
    temp.clear();
    for(int i = 0;i<(int)nums.size();i++)
    {
        for(int j:nums[i])
        {   bool flag = true;
            for (vector<int> t1:temp)
            {
                if((t1[0]==i && t1[1]==j) ||(t1[0]==j && t1[1] == i))
                {
                    flag = false;
                }
            }
            if(flag)
            {
                vector<int> t{i,j};
                temp.push_back(t);
                t.clear();
            }

        }
    }
    return temp;
}
void vertex_cover(std::vector<std::vector<int>> nums)
{
    int m = nums.size();
    int high = m;
    int low = 1;
    vector<int> vertices;
    vertices.clear();
    while(low<=high)
    {
        int k = int(low+high)/2;
        Minisat::Solver solver;
        std::vector<std::vector<Minisat::Lit>> atms(m);
        for (int i = 0;i<m;i++)
        {
            for(int j = 0;j<k;j++)
            {
                atms[i].push_back(Minisat::mkLit(solver.newVar()));
            }
        }
        // clause 1
        for(int i = 0;i<k;i++)
        {
            Minisat::vec<Minisat::Lit> temp1;
           for(int j = 0;j<m;j++)
           {
               temp1.push(atms[j][i]);
           }
           solver.addClause(temp1);
           temp1.clear();
        }
        //clause 2
        for(int i = 0;i<m;i++)
        {
            for(int p = 0;p<k-1;p++)
            {
                for (int q = p+1;q<k;q++)
                {
                    solver.addClause(~atms[i][p],~atms[i][q]);
                }
            }
        }
        //clause 3
        for(int i = 0;i<k;i++)
        {
            for(int p = 0;p<m-1;p++)
            {
                for(int q = p+1;q<m;q++)
                {
                    solver.addClause(~atms[p][i],~atms[q][i]);
                }
            }
        }
        //clause 4
        vector<vector<int>> temp2  = create_edges(nums);
        for(int i = 0;i<temp2.size();i++)
        {
            int v1 = temp2[i][0];
            int v2 = temp2[i][1];
            Minisat::vec<Minisat::Lit> v_tmp;
            for(int p = 0;p<k;p++)
            {
                v_tmp.push(atms[v1][p]);
                v_tmp.push(atms[v2][p]);
            }
            solver.addClause(v_tmp);
            v_tmp.clear();
        }
        temp2.clear();
        bool result = solver.solve();
        if(result)
        {
            high = k-1;
            vertices.clear();
            for(int i = 0; i < m; i++)
                {
                    for(int j = 0; j < k; j++)
                        {
                            Minisat::lbool tf=solver.modelValue(atms[i][j]);
                            if(tf==Minisat::l_True)
                                {   
                                    vertices.push_back(i);
                                }

                        }
                }
        }
        else
        {
            low = k+1;

        }
    }
    for(int i = 0;i<vertices.size();i++)
    {
        cout << vertices[i]+1 <<" ";
    }
    cout << endl;
    vertices.clear();
}
 

int main()
 {
    std::vector<std::vector<int>> nums;
        // print a promt
        // read a line of input until EOL and store in a string
    while(!std::cin.eof())
    {
        std::string line;
        std::getline(std::cin, line);
        std::istringstream input(line);
        string temp;
        while(!input.eof())
        {
            input >> temp;
            //cout << "The input is " << temp << '\n';
            if (temp[0]=='V')
                {
                    int length;
                    input >> length;
                    if(length > 0)
                    {
                        nums.clear();
                        nums.resize(length);
                        //cout << "The size of array is" << nums.size();
                    }
                    else
                    {
                        cout << "Error: There should be atleast one vertex"<< '\n';
                        break;
                    }
                }// End for vertex
            if (temp[0] == 'E')
            {
                 if(nums.size() == 0)
                        {
                            cout << "Error: Please Enter the number of vertices first" << '\n';
                            break;
                        }
                input >> temp;
                try
                {
                    int result = create_adjacencylist(nums,temp);
                    if(result == -1)
                    {
                        cout << "Error: Please enter the correct edges" << '\n';
                        break;
                    }
                    else
                    {
                        vertex_cover(nums);
                    }
                }
                catch(const std::exception& e)
                {
                    std::cout<<endl;
                }
                
                

            }
        }
    }
return 0;
}