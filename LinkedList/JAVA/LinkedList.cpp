// #include <bits/stdc++.h>
// using namespace std;

// struct node
// {
//     string info;
//     struct node *next;
// };

// node *top;

// void push(string data)
// {
//     node *temp = new node();
//     if (!temp)
//     {
//         cout << "\nStack Overflow";
//         exit(1);
//     }
//     temp->info = data;
//     temp->next = top;
//     top = temp;
// }
// void pop()
// {
//     node *temp;
//     if (top == NULL)
//     {
//         cout << "\nStack Underflow" << endl;
//         exit(1);
//     }
//     else
//     {
//         temp = top;
//         top = top->next;
//         free(temp);
//     }
// }

// void display()
// {
//     node *temp;

//     if (top == NULL)
//     {
//         cout << "\nStack Underflow";
//         exit(1);
//     }
//     else
//     {
//         temp = top;
//         while (temp != NULL)
//         {

//             cout << temp->info << "-> ";
//             temp = temp->next;
//         }
//         cout << "\n";
//     }
// }
// int main()
// {
//     // Push the elements of stack
//     push("vi");
//     push("si");
//     push("ku");
//     push("he");

//     // Display stack elements
//     display();

//     // Delete top elements of stack
//     pop();
//     pop();

//     // Display stack elements
//     display();

//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

struct node
{
    string info;
    node *next;
    node(string d)
    {
        info = d;
        next = NULL;
    }
};

struct Queue
{
    node *front, *rear;
    Queue()
    {
        front = rear = NULL;
    }

    void enQueue(string x)
    {
        node *temp = new node(x);
        if (rear == NULL)
        {
            front = rear = temp;
            return;
        }
        rear->next = temp;
        rear = temp;
    }
};
int main()
{
    Queue q;
    q.enQueue("a");
    q.enQueue("b");
    q.enQueue("c");
    q.enQueue("d");
    q.enQueue("e");
    cout << "Queue Front : " << (q.front)->info << endl;
    cout << "Queue Rear : " << (q.rear)->info;
}
