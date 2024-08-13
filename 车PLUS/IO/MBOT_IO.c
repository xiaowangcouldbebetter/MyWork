#include "MBOT_IO.h"
extern int a,b,c,d,e,f,g;

void MBOT_IO_Init(void)
{
  GPIO_InitTypeDef MBOTIO;
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOD|RCC_APB2Periph_GPIOC|RCC_APB2Periph_GPIOE|RCC_APB2Periph_GPIOA,ENABLE); 

	//P5
	MBOTIO.GPIO_Pin=GPIO_Pin_10|GPIO_Pin_11;//左上
	MBOTIO.GPIO_Mode=GPIO_Mode_Out_PP;
	MBOTIO.GPIO_Speed=GPIO_Speed_50MHz;
	GPIO_Init(GPIOD,&MBOTIO);
		
	MBOTIO.GPIO_Pin=GPIO_Pin_0;
	MBOTIO.GPIO_Mode=GPIO_Mode_Out_PP;
	MBOTIO.GPIO_Speed=GPIO_Speed_50MHz;
	GPIO_Init(GPIOA,&MBOTIO);
		

	MBOTIO.GPIO_Pin=GPIO_Pin_4|GPIO_Pin_5;
	MBOTIO.GPIO_Mode=GPIO_Mode_Out_PP;
	MBOTIO.GPIO_Speed=GPIO_Speed_50MHz;
	GPIO_Init(GPIOC,&MBOTIO);
	
	MBOTIO.GPIO_Pin=GPIO_Pin_8|GPIO_Pin_15|GPIO_Pin_7;//右下
	MBOTIO.GPIO_Mode=GPIO_Mode_Out_PP;
	MBOTIO.GPIO_Speed=GPIO_Speed_50MHz;
	GPIO_Init(GPIOE,&MBOTIO);
	
	/*传感器IO*/
	
	GPIO_PinRemapConfig(GPIO_Remap_PD01,ENABLE);
	GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable,ENABLE);  //禁用JTAG 启用 SWD
	MBOTIO.GPIO_Pin=GPIO_Pin_0|GPIO_Pin_1|GPIO_Pin_2|GPIO_Pin_3|GPIO_Pin_4|GPIO_Pin_5|GPIO_Pin_7;
	MBOTIO.GPIO_Mode=GPIO_Mode_IN_FLOATING;
	GPIO_Init(GPIOD,&MBOTIO);
	
}
void STOP(void)
{

	//左上
		TIM_SetCompare4 (TIM3,0);
		GPIO_ResetBits(GPIOD,GPIO_Pin_10);
		GPIO_ResetBits(GPIOD,GPIO_Pin_11);

			//右上
		TIM_SetCompare2 (TIM3,0);
		GPIO_ResetBits(GPIOC,GPIO_Pin_5);
		GPIO_ResetBits(GPIOC,GPIO_Pin_4);
		
			//左下
		TIM_SetCompare1 (TIM3,0);
		GPIO_ResetBits(GPIOA,GPIO_Pin_0);
		GPIO_ResetBits(GPIOE,GPIO_Pin_7);
		
			//右下
		TIM_SetCompare3 (TIM3,0);
		GPIO_ResetBits(GPIOE,GPIO_Pin_15);
		GPIO_ResetBits(GPIOE,GPIO_Pin_8);
}

void regrogress(void)
{
		//左上
		TIM_SetCompare4 (TIM3,600);
		GPIO_SetBits(GPIOD,GPIO_Pin_11);
		GPIO_ResetBits(GPIOD,GPIO_Pin_10);

			//右上
		TIM_SetCompare2 (TIM3,600);
		GPIO_SetBits(GPIOC,GPIO_Pin_4);
		GPIO_ResetBits(GPIOC,GPIO_Pin_5);
		
			//左下
		TIM_SetCompare1 (TIM3,600);
		GPIO_SetBits(GPIOA,GPIO_Pin_7);
		GPIO_ResetBits(GPIOE,GPIO_Pin_0);
		
			//右下
		TIM_SetCompare3 (TIM3,600);
		GPIO_SetBits(GPIOE,GPIO_Pin_8);
		GPIO_ResetBits(GPIOE,GPIO_Pin_15);
	
}
void FORDWARD(void)
{
			//左上
		TIM_SetCompare4 (TIM3,500);//700
		GPIO_SetBits(GPIOD,GPIO_Pin_10);
		GPIO_ResetBits(GPIOD,GPIO_Pin_11);

			//右上
		TIM_SetCompare2 (TIM3,500);
		GPIO_SetBits(GPIOC,GPIO_Pin_5);
		GPIO_ResetBits(GPIOC,GPIO_Pin_4);
		
			//左下
		TIM_SetCompare1 (TIM3,500);
		GPIO_SetBits(GPIOA,GPIO_Pin_0);
		GPIO_ResetBits(GPIOE,GPIO_Pin_7);
		
			//右下
		TIM_SetCompare3 (TIM3,500);
		GPIO_SetBits(GPIOE,GPIO_Pin_15);
		GPIO_ResetBits(GPIOE,GPIO_Pin_8);
}


void TURNLEFT(void)
{
	//左上
		TIM_SetCompare4 (TIM3,400);
		GPIO_SetBits(GPIOD,GPIO_Pin_11);
		GPIO_ResetBits(GPIOD,GPIO_Pin_10);

			//右上
		TIM_SetCompare2 (TIM3,500);
		GPIO_SetBits(GPIOC,GPIO_Pin_5);
		GPIO_ResetBits(GPIOC,GPIO_Pin_4);
		
			//左下
		TIM_SetCompare1 (TIM3,400);
		GPIO_ResetBits(GPIOA,GPIO_Pin_0);
		GPIO_SetBits(GPIOE,GPIO_Pin_7);
		
			//右下
		TIM_SetCompare3 (TIM3,500);
		GPIO_SetBits(GPIOE,GPIO_Pin_15);
		GPIO_ResetBits(GPIOE,GPIO_Pin_8);
}
void turnleft(void)
{
			//左上
		TIM_SetCompare4 (TIM3,200);
		GPIO_SetBits(GPIOD,GPIO_Pin_10);
		GPIO_ResetBits(GPIOD,GPIO_Pin_11);

			//右上
		TIM_SetCompare2 (TIM3,400);
		GPIO_SetBits(GPIOC,GPIO_Pin_5);
		GPIO_ResetBits(GPIOC,GPIO_Pin_4);
		
			//左下
		TIM_SetCompare1 (TIM3,200);
		GPIO_SetBits(GPIOA,GPIO_Pin_0);
		GPIO_ResetBits(GPIOE,GPIO_Pin_7);
		
			//右下
		TIM_SetCompare3 (TIM3,400);
		GPIO_SetBits(GPIOE,GPIO_Pin_15);
		GPIO_ResetBits(GPIOE,GPIO_Pin_8);
}

void TURNRIGHT(void)
{

		//左上
		TIM_SetCompare4 (TIM3,500);
		GPIO_SetBits(GPIOD,GPIO_Pin_10);
		GPIO_ResetBits(GPIOD,GPIO_Pin_11);

			//右上
		TIM_SetCompare2 (TIM3,400);
		GPIO_SetBits(GPIOC,GPIO_Pin_4);
		GPIO_ResetBits(GPIOC,GPIO_Pin_5);
		
			//左下
		TIM_SetCompare1 (TIM3,500);
		GPIO_SetBits(GPIOA,GPIO_Pin_0);
		GPIO_ResetBits(GPIOE,GPIO_Pin_7);
		
			//右下
		TIM_SetCompare3 (TIM3,400);
		GPIO_SetBits(GPIOE,GPIO_Pin_8);
		GPIO_ResetBits(GPIOE,GPIO_Pin_15);
}
void turnright(void)
{
			//左上
		TIM_SetCompare4 (TIM3,400);
		GPIO_SetBits(GPIOD,GPIO_Pin_10);
		GPIO_ResetBits(GPIOD,GPIO_Pin_11);

			//右上
		TIM_SetCompare2 (TIM3,200);
		GPIO_SetBits(GPIOC,GPIO_Pin_5);
		GPIO_ResetBits(GPIOC,GPIO_Pin_4);
		
			//左下
		TIM_SetCompare1 (TIM3,400);
		GPIO_SetBits(GPIOA,GPIO_Pin_0);
		GPIO_ResetBits(GPIOE,GPIO_Pin_7);
		
			//右下
		TIM_SetCompare3 (TIM3,200);
		GPIO_SetBits(GPIOE,GPIO_Pin_15);
		GPIO_ResetBits(GPIOE,GPIO_Pin_8);
}

void STATE(void)
{   
	
		a	=	GPIO_ReadInputDataBit(GPIOD,  GPIO_Pin_0);
		b =	GPIO_ReadInputDataBit(GPIOD,  GPIO_Pin_1);
		c	=	GPIO_ReadInputDataBit(GPIOD,  GPIO_Pin_2);
		d	=	GPIO_ReadInputDataBit(GPIOD,  GPIO_Pin_3);
		e	=	GPIO_ReadInputDataBit(GPIOD,  GPIO_Pin_4);
		f	=	GPIO_ReadInputDataBit(GPIOD,  GPIO_Pin_5);
		g	=	GPIO_ReadInputDataBit(GPIOD,  GPIO_Pin_6);



}
