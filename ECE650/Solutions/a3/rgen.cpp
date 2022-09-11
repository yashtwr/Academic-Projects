// Name of program mainreturn.cpp
#include <iostream>
#include <sstream>
#include<time.h>
#include<unistd.h>
using namespace std;
bool isNumber(const string& s)
{
    for (char const &ch : s) {
        if (std::isdigit(ch) == 0) 
            return false;
    }
    return true;
 }
 void read_commandline(int &argc,char *argv[],int &streets,int &line_sgmts,int &wait_sec,int &coord)
 {  
     for (int i = 0; i < argc; i++)
    {
        std:: string temp = argv[i];
        if(temp.compare("-s")==0)
        {
            if(isNumber(argv[i+1]))
            {
                std::stringstream num(argv[i+1]);
                num >> streets;
            }
            else{
                cerr << "Error: Invalid input type";
            }
        }
        else if(temp.compare("-n") == 0)
        {
            if(isNumber(argv[i+1]))
            {
                std::stringstream num(argv[i+1]);
                num >> line_sgmts;
            }
            else{
                cerr << "Error: Invalid input type";
            }
        }
        else if(temp.compare("-l") == 0)
        {
            if(isNumber(argv[i+1]))
            {
                std::stringstream num(argv[i+1]);
                num >> wait_sec;
            }
            else{
                cerr << "Error: Invalid input type";
            }
        }
        else if(temp.compare("-c") == 0)
        {
            if(isNumber(argv[i+1]))
            {
                std::stringstream num(argv[i+1]);
                num >> coord;
            }
            else{
                cerr << "Error: Invalid input type";
            }
        }
        else if (isNumber(temp))
        {
            continue;
        }
    }
 }
 void update_inputs(int &streets,int &line_sgmts,int &wait_sec)
 {
    srand (time(NULL));
    streets = 2 + rand()%(streets+2-1);
    wait_sec = 5+rand()%(wait_sec-5+1);
    line_sgmts = 1 + rand()%line_sgmts;

 }
 void generate_street_names(int streets,string street_names[])
 {
     street_names[0] = "aa";
    for(int i = 1;i<streets;i++)
    {
        string str = street_names[i-1];
        char c = str[str.length()-1];
        if( c == 'z')
        {
            street_names[i] = str + 'a';
        }
        else{
            street_names[i] = str.substr(0,str.length()-1) + char(c+1);
        }
        
    }
 }
 void create_streets(int streets,int l,int c,string street_names[])
 {
     
    //generating names
    int coord[streets][l][2];
    generate_street_names(streets,street_names);
    for(int i = 0;i<streets;i++)
    {
        for(int j = 0;j<=l;j++)
        {
            int x = -c + (rand()%(c+c-1));
            int y = -c + (rand()%(c+c-1));
            coord[i][j][0] = x;
            coord[i][j][1] = y;
            cout <<"( "<<x<<","<<y<<") ";
        }
        cout <<endl;
    }

    
 }

int main(int argc, char* argv[])
{
	int streets = 10;
    int line_sgmts = 5;
    int wait_sec = 5;
    int coord = 20;
    read_commandline(argc,argv,streets,line_sgmts,wait_sec,coord);
    //while(true)
    //{
    update_inputs(streets,line_sgmts,wait_sec);
    string street_names[streets]; 
    create_streets(streets,line_sgmts,coord,street_names);
    //}
	return 0;
}
