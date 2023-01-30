class Person

{

private:

    string name_;

    int age_;

public:

    Person(const string& name, int age); // 기초 클래스 생성자의 선언

    void ShowPersonInfo();

};

 

class Student : public Person

{

private:

    int student_id_;

public:

    Student(int sid, const string& name, int age); // 파생 클래스 생성자의 선언

};