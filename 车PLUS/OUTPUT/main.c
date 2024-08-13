#include "PWM.h"
#include "delay.h"
//#include "encoder.h"
#include "timer.h"
#include <stdio.h>
#include "MBOT_IO.h"
#include "oled.h" 
#include "usart.h"
#include "sys.h"
#include "stm32f10x_i2c.h"              // Keil::Device:StdPeriph Drivers:I2C
#include "stm32f10x.h" 
 
 
 /*串口用
len：数据长度
Res
*/
u16 t,len;
u8 Res;

void USART_GET(void);
//int leftSpeedNow  =0;
//int rightSpeedNow =0;

char str1[20];
//char str2[20];
int a,b,c,d,e,f,g,z;
int i=0;

//超声波
//float length_1 = 0;

int main(void)
{ 

	
//	OLED_Init();//屏幕初始化
//	OLED_Clear();//OLED清屏	

	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);	//=====设置中断分组
	MBOT_IO_Init();
	Hcsr06Init();
	delay_init();	    	        //=====延时函数初始化                  
  PWM_GPIOInitial();
  TIM3_Initial();
  PWM_Initial();
	uart_init(9600);
//	Encoder_Init_TIM1();            //=====初始化编码器1接口
//	Encoder_Init_TIM4();            //=====初始化编码器2接口
	
	TIM2_Int_Init(1000,72);     //=====定时器初始化 5ms一次中断
//	FORDWARD();
//	delay_ms (500);
	while(1)
	{ 

//	USART_GET();

		STATE();
		
		 if(a==1&&b==1&&c==1&&d==0&&e==1&&f==1&&g==1)
		{
			FORDWARD();
		}
		else if((a==1&&e==1&&f==1&&g==1)&&(b==0||c==0))
		{
			turnleft();
		}
		else if((a==1&&b==1&&c==1&&g==1)&&(e==0||f==0))
		{
			turnright();
		}
		else if((a==0&&b==0&&c==0)&&(e==1||f==1||g==1||d==0))
		{	
			delay_ms(100);
			if((a==0&&b==0&&c==0)&&(e==1||f==1||g==1||d==0))
			{
				TURNLEFT()	;
				delay_ms(200);
			}
		}
		else if((a==1||b==1||c==1||d==0)&&(e==0&&f==0&&g==0))
		{
			delay_ms(100);
			if(a==0&&b==0&&c==0&&d==0&&e==0&&f==0&&g==0)
				{ 
					STATE();
					if(i>1)
					 {
						STOP();
					 }
						
					if(i==1)
					 {	
						TURNRIGHT();
						delay_ms (500);
					 }
						FORDWARD();
						delay_ms (200);
						i++;	
				}
				TURNRIGHT()	;
				delay_ms(200);
		
		}
		


		
	}
}


/*串口接收函数*/
void USART_GET(void)
{
		if(USART_RX_STA)
		{
				if(USART_RX_BUF[0]=='f'&& USART_RX_BUF[1]=='o')
				{
					t=1;
					USART_RX_STA=0;
				}
				else 
			if(USART_RX_BUF[0]=='s'&& USART_RX_BUF[1]=='t')
				{ 
					t=2;
					USART_RX_STA=0;
	
				}
				else if(USART_RX_BUF[0]=='b'&& USART_RX_BUF[1]=='a')
				{ 
					t=3;
					USART_RX_STA=0;	
				}
				else if(USART_RX_BUF[0]=='l'&& USART_RX_BUF[1]=='e')
				{ 
					t=4;
					USART_RX_STA=0;	
				}
				else if(USART_RX_BUF[0]=='r'&& USART_RX_BUF[1]=='i')
				{ 
					t=5;
					USART_RX_STA=0;	
				}
			STOP();
			FORDWARD();
			TURNLEFT();
			TURNRIGHT();
		
		if(t ==1)
		{
					FORDWARD();
			}
		else 
			if(t ==2)
			{
					STOP();
			}
		else if(t ==3)
			{
					regrogress();
			}
		else if(t ==4)
			{
					TURNLEFT();
			}
		else if(t ==5)
			{
					TURNRIGHT();
			}
		}


}

