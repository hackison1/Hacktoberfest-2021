#include<stdio.h>
#include<stdlib.h>
struct STUDENT{
	int id, roll_no, phone_no,choice;
	float percent;
	char name[50], address[50], father[50], mother[50], email[50], gender[10];
};

void getdetail(struct STUDENT S[]){
	int i;
	for(i=0;i<2;i++)
	{
		fflush(stdin);
		printf("\nEnter the details of student no. %d...\n",i+1);
		printf("Enter your name: ");
		gets(S[i].name);
		printf("Enter your father's name: ");
		gets(S[i].father);
		printf("Enter your mother's name: ");
		gets(S[i].mother);
		printf("Enter your address: ");
		gets(S[i].address);
		printf("Enter your email address: ");
		gets(S[i].email);
		printf("Enter your gender: ");
		gets(S[i].gender);
		printf("Enter your student id: ");
		scanf("%d",&S[i].id);
		printf("Enter your percentage: ");
		scanf("%f",&S[i].percent);
		printf("Enter your roll no: ");
		scanf("%d",&S[i].roll_no);	
		printf("Enter your contact number: ");
		scanf("%d",&S[i].phone_no);
	}
}
void displaydetail(struct STUDENT S[]){
	int i;
	printf("\n\n\n \xDB ****** STUDENT DETAILS ****** \xDB\n\n\n");
	for(i=0;i<2;i++){
		fflush(stdin);
		printf("\nName:              %s",S[i].name);
		printf("\nFather's name:     %s",S[i].father);
		printf("\nMother's name:     %s",S[i].mother);
		printf("\nAddress:           %s",S[i].address);
		printf("\nE-mail:            %s",S[i].email);
		printf("\nGender:            %s",S[i].gender);
		printf("\n\nStudent's Id:    %s",S[i].id);
		printf("\nPercentage:        %.3f%%",S[i].percent);
		printf("\nRoll no:           %d",S[i].roll_no);
		printf("\nContact number:    %d",S[i].phone_no);
	}
	system("pause");
}

void gradesheet(struct STUDENT S[]){
	int i;
	float gpa;
	printf("\n\n\n \xDB ****** GRADE SHEET ****** \xDB");
	for(i=0;i<2;i++){
		gpa = (S[i].percent)/100*4.0;
		if (gpa>=3.6){
			printf("\n\nStudent's Id:     %d",S[i].id);
			printf("\nName:             %s",S[i].name);
			printf("\nGPA:              %.2f",gpa);
			printf("\nGrade:            A+\n");
		}
		else if (gpa>=3.2 && gpa<3.6){
			printf("\n\nStudent's Id:     %d",S[i].id);
			printf("\nName:             %s",S[i].name);
			printf("\nGPA:              %.2f",gpa);
			printf("\nGrade:            A\n");
		}
		else if (gpa>=2.8 && gpa<3.2){
			printf("\n\nStudent's Id:     %d",S[i].id);
			printf("\nName:             %s",S[i].name);
			printf("\nGPA:              %.2f",gpa);
			printf("\nGrade:            B+\n");
		}
		else if (gpa>=2.4 && gpa<2.8){
			printf("\n\nStudent's Id:     %d",S[i].id);
			printf("\nName:             %s",S[i].name);
			printf("\nGPA:              %.2f",gpa);
			printf("\nGrade:            B\n");
		}
		else if (gpa>=2.0 && gpa<2.4){
			printf("\n\nStudent's Id:     %d",S[i].id);
			printf("\nName:             %s",S[i].name);
			printf("\nGPA:              %.2f",gpa);
			printf("\nGrade:            C+\n");
		}
		else if (gpa>=1.6 && gpa<2.0){
			printf("\n\nStudent's Id:     %d",S[i].id);
			printf("\nName:             %s",S[i].name);
			printf("\nGPA:              %.2f",gpa);
			printf("\nGrade:            C\n");
		}
		else if (gpa>=1.2 && gpa<1.6){
			printf("\n\nStudent's Id:     %d",S[i].id);
			printf("\nName:             %s",S[i].name);
			printf("\nGPA:              %.2f",gpa);
			printf("\nGrade:            D+\n");
		}
		else if (gpa>=0.8 && gpa<1.2){
			printf("\n\nStudent's Id:     %d",S[i].id);
			printf("\nName:             %s",S[i].name);
			printf("\nGPA:              %.2f",gpa);
			printf("\nGrade:            D\n");
		}
		else{
			printf("\n\nStudent's Id:     %d",S[i].id);
			printf("\nName:             %s",S[i].name);
			printf("\nGPA:              %.2f",gpa);
			printf("\nGrade:            E(FAIL)\n");
		}
	}
}
void main(){
	struct STUDENT S[2];
	int choice;
	printf("\n\t\t\t\t\t\t**********************************\t\t\t\n");
	printf("\t\t\t\t\t\t\t\xB2 ****** MENU ****** \xB2\t\t\t");
	printf("\n\t\t\t\t\t\t**********************************\t\t\t\n");
	printf("\n\nChoose the option:\n\n(1)Input Student Details\t(2)Display Student details\t(3)Display gradesheet\t(4)Display both\t(5)Exit\n\n");
	printf("Enter your choice here..............: ");
	scanf("%d",&choice);
	while (1){
	switch(choice){
		case 1:
			system("color b4");
			getdetail(S);
			printf("\n\n\nBack to Menu...!!..");
			system("pause");
			printf("\n\t\t\t\t\t\t**********************************\t\t\t\n");
			printf("\t\t\t\t\t\t\t\xB2 ****** MENU ****** \xB2\t\t\t");
			printf("\n\t\t\t\t\t\t**********************************\t\t\t\n");
			printf("\n\nChoose the option:\n\n(1)Input Student Details\t(2)Display Student details\t(3)Display gradesheet\t(4)Display both\t(5)Exit\n\n");
			printf("Enter your choice here..............: ");
			scanf("%d",&choice);
		case 2:
			system("color b0");
			displaydetail(S);
			system("pause");
		case 3:
			system("color b0");
			gradesheet(S);
			printf("\n\n\nBack to Menu...!!..");
			system("pause");
			printf("\n\t\t\t\t\t\t**********************************\t\t\t\n");
			printf("\t\t\t\t\t\t\t\xB2 ****** MENU ****** \xB2\t\t\t");
			printf("\n\t\t\t\t\t\t**********************************\t\t\t\n");
			printf("\n\nChoose the option:\n\n(1)Input Student Details\t(2)Display Student details\t(3)Display gradesheet\t(4)Display both\t(5)Exit\n\n");
			printf("Enter your choice here..............: ");
			scanf("%d",&choice);
		case 4:
			system("color b0");
			displaydetail(S);
			printf("\n\nNow, for gradesheet... ");
			system("pause");
			gradesheet(S);
			system("pause");
			printf("\n\t\t\t\t\t\t**********************************\t\t\t\n");
			printf("\t\t\t\t\t\t\t\xB2 ****** MENU ****** \xB2\t\t\t");
			printf("\n\t\t\t\t\t\t**********************************\t\t\t\n");
			printf("\n\nChoose the option:\n\n(1)Input Student Details\t(2)Display Student details\t(3)Display gradesheet\t(4)Display both\t(5)Exit\n\n");
			printf("Enter your choice here..............: ");
			scanf("%d",&choice);
		case 5:
			system("color 40");
			break;
		default:
			system("color 4");
			printf("\n\n\n\n\n\t\t\t\tOption out of range!!\n\n\n\n");
			printf("\n\n\nBack to Menu...!!..");
			system("pause");
			system("color b4");
			printf("\n\t\t\t\t\t\t**********************************\t\t\t\n"); 
			printf("\t\t\t\t\t\t\t\xB2 ****** MENU ****** \xB2\t\t\t");
			printf("\n\t\t\t\t\t\t**********************************\t\t\t\n");
			printf("\n\nChoose the option:\n\n(1)Input Student Details\t(2)Display Student details\t(3)Display gradesheet\t(4)Display both\t(5)Exit\n\n");
			printf("Enter your choice here..............: ");
			scanf("%d",&choice);
		}
	}
	exit (0);
}