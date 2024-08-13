#include "encoder.h"

/**************************************************************************
函数功能：把TIM1初始化为编码器接口模式
**************************************************************************/
void Encoder_Init_TIM1(void)
{
	TIM_TimeBaseInitTypeDef TIM_TimeBaseStructure;  
	TIM_ICInitTypeDef TIM_ICInitStructure;  
	GPIO_InitTypeDef GPIO_InitStructure;
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_TIM1, ENABLE);    //使能定时器1的时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOE|RCC_APB2Periph_AFIO, ENABLE);   //使能PE端口时钟
	GPIO_PinRemapConfig(GPIO_FullRemap_TIM1,ENABLE);

	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9|GPIO_Pin_11;	//端口配置
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;   //浮空输入
	GPIO_Init(GPIOE, &GPIO_InitStructure);					//根据设定参数初始化GPIOA

	TIM_TimeBaseStructInit(&TIM_TimeBaseStructure);
	TIM_TimeBaseStructure.TIM_Prescaler = 0x0;              //预分频器 
	TIM_TimeBaseStructure.TIM_Period = ENCODER_TIM_PERIOD;  //设定计数器自动重装值
	TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1; //选择时钟分频：不分频
	TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;////TIM向上计数  
	TIM_TimeBaseStructure.TIM_RepetitionCounter = 0;
	TIM_TimeBaseInit(TIM1, &TIM_TimeBaseStructure);
	
	TIM_EncoderInterfaceConfig(TIM1, TIM_EncoderMode_TI12, TIM_ICPolarity_Rising, TIM_ICPolarity_Rising);//使用编码器模式3
	
	TIM_ICStructInit(&TIM_ICInitStructure);
	TIM_ICInitStructure.TIM_ICFilter = 10;
	TIM_ICInit(TIM1, &TIM_ICInitStructure);
	
	TIM_ClearFlag(TIM1, TIM_FLAG_Update);                   //清除TIM的更新标志位
	TIM_ITConfig(TIM1, TIM_IT_Update, ENABLE);

	TIM_SetCounter(TIM1,0);
	TIM_Cmd(TIM1, ENABLE); 
}
/**************************************************************************
函数功能：把TIM4初始化为编码器接口模式
**************************************************************************/
void Encoder_Init_TIM4(void)
{
	TIM_TimeBaseInitTypeDef TIM_TimeBaseStructure;  
	TIM_ICInitTypeDef TIM_ICInitStructure;  
	GPIO_InitTypeDef GPIO_InitStructure;
	
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM4, ENABLE);    //使能定时器4的时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOD|RCC_APB2Periph_AFIO, ENABLE);   //使能PD端口时钟
	GPIO_PinRemapConfig(GPIO_Remap_TIM4,ENABLE);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_12|GPIO_Pin_13;	//端口配置
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;   //浮空输入
	GPIO_Init(GPIOD, &GPIO_InitStructure);					//根据设定参数初始化GPIOB

	TIM_TimeBaseStructInit(&TIM_TimeBaseStructure);
	TIM_TimeBaseStructure.TIM_Prescaler = 0x0;              // 预分频器 
	TIM_TimeBaseStructure.TIM_Period = ENCODER_TIM_PERIOD;  //设定计数器自动重装值
	TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1; //选择时钟分频：不分频
	TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;////TIM向上计数  
	TIM_TimeBaseInit(TIM4, &TIM_TimeBaseStructure);
	TIM_EncoderInterfaceConfig(TIM4, TIM_EncoderMode_TI12, TIM_ICPolarity_Rising, TIM_ICPolarity_Rising);//使用编码器模式
	TIM_ICStructInit(&TIM_ICInitStructure);
	TIM_ICInitStructure.TIM_ICFilter = 10;
	TIM_ICInit(TIM4, &TIM_ICInitStructure);
	TIM_ClearFlag(TIM4, TIM_FLAG_Update);                   //清除TIM的更新标志位
	TIM_ITConfig(TIM4, TIM_IT_Update, ENABLE);

	TIM_SetCounter(TIM4,0);
	TIM_Cmd(TIM4, ENABLE); 
}

/**************************************************************************
函数功能：读取编码器脉冲差值
**************************************************************************/
//s16 getTIMx_DetaCnt(TIM_TypeDef * TIMx)
//{
//	s16 cnt;
//	cnt = TIMx->CNT-0x7fff;
//	TIMx->CNT = 0x7fff;
//	return cnt;
//}
int Read_Encoder(u8 TIMX)
{
int Encoder_TIM;
	switch(TIMX)
	{
		case 1:Encoder_TIM=(short )TIM1 ->CNT; TIM1 ->CNT =0;break;
		case 4:Encoder_TIM=(short )TIM4 ->CNT; TIM4 ->CNT =0;break;
		default:Encoder_TIM=0;
	}
	return Encoder_TIM;
}

