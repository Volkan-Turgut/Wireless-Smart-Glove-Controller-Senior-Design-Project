// Slave as receiver for SPI communitation
#include <stdio.h>
#include <esp_system.h>
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
#include <string.h>

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/semphr.h"
#include "freertos/queue.h"

#include "lwip/sockets.h"
#include "lwip/dns.h"
#include "lwip/netdb.h"
#include "lwip/igmp.h"

#include "esp_wifi.h"
#include "esp_system.h"
#include "esp_event.h"
#include "nvs_flash.h"
#include "soc/rtc_periph.h"
#include "driver/spi_slave.h"
#include "esp_log.h"
#include "spi_flash_mmap.h"
#include "driver/gpio.h"
#include "esp_netif.h"
#include "mqtt_client.h"

// Pins in use
#define GPIO_MOSI 23
#define GPIO_MISO 19
#define GPIO_SCLK 18
#define GPIO_CS 5

#include <stdio.h>
#include <string.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_wifi.h"
#include "esp_event.h"
#include "esp_log.h"
#include "nvs_flash.h"
#include "mqtt_client.h"

#define SSID "volkanpc"
#define PASSWORD "12345678"
static const char *TAG = "MQTT_EXAMPLE";

#define GPIO_OUTPUT_PIN  GPIO_NUM_12
#define GPIO_INPUT_PIN   GPIO_NUM_26

//static esp_mqtt_client_handle_t client;
//
//esp_mqtt_client_config_t mqtt_cfg = {
//    .broker.address.uri = "mqtt://127.0.0.1",
//    .broker.address.hostname = "127.0.0.1",
//    .broker.address.port = 1883,
//};
//
//
//void wifi_init_sta(void)
//{
//    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
//    esp_wifi_init(&cfg);
//    esp_event_handler_t wifi_event_handler;
//    esp_event_handler_register(WIFI_EVENT, ESP_EVENT_ANY_ID, &wifi_event_handler, NULL);
//
//    wifi_config_t wifi_config = {
//        .sta = {
//            .ssid = SSID,
//            .password = PASSWORD,
//        },
//    };
//
//    esp_wifi_set_mode(WIFI_MODE_STA);
//    esp_wifi_set_config(ESP_IF_WIFI_STA, &wifi_config);
//    esp_wifi_start();
//}
void app_main(void)
{
    printf("ESP-IDF version: %s\n", (char *)ESP_IDF_VERSION);

//	ESP_ERROR_CHECK(nvs_flash_init());
//	wifi_init_sta();
//	client = esp_mqtt_client_init(&mqtt_cfg);
//	esp_mqtt_client_start(client);    //Configuration for the SPI bus
//    vTaskDelay(pdMS_TO_TICKS(10)); // Delay for 10 ms
//    const char* message="yarragımı ye sarp";
//    esp_mqtt_client_publish(client, "sarp yarak", message, strlen(message), 0, 0);
//	esp_rom_gpio_pad_select_gpio(GPIO_INPUT_PIN);
//    gpio_set_direction(GPIO_INPUT_PIN, GPIO_MODE_INPUT);
//	esp_rom_gpio_pad_select_gpio(GPIO_OUTPUT_PIN);
//    gpio_set_direction(GPIO_OUTPUT_PIN, GPIO_MODE_INPUT_OUTPUT);
//
//    gpio_set_level(GPIO_OUTPUT_PIN, 0);  // Set output level to high
//	spi_bus_config_t buscfg={
//        .mosi_io_num=GPIO_MOSI,
//        .miso_io_num=GPIO_MISO,
//        .sclk_io_num=GPIO_SCLK,
//        .quadwp_io_num = -1,
//        .quadhd_io_num = -1,
//    };
//
//    //Configuration for the SPI slave interface
//    spi_slave_interface_config_t slvcfg={
//        .mode=0,
//        .spics_io_num=GPIO_CS,
//        .queue_size=8,
//        .flags=0,
//    };
//
//    //Initialize SPI slave interface
//    spi_slave_initialize(VSPI_HOST, &buscfg, &slvcfg, SPI_DMA_CH_AUTO);
//
//    char recvbuf[129]="";
//    memset(recvbuf, 0, 33);
//    spi_slave_transaction_t t;
//    memset(&t, 0, sizeof(t));
//
//	printf("Slave output:\n");
//    while(1) {
//    	int input_level=gpio_get_level(GPIO_INPUT_PIN);
//    	int output_level=gpio_get_level(GPIO_OUTPUT_PIN);
//    	if(input_level!=output_level){
//    		gpio_set_level(GPIO_OUTPUT_PIN, input_level);
//    		printf("Change Detected\n");
//    	}



//        t.length=128*8;
//        t.rx_buffer=recvbuf;
//        spi_slave_transmit(VSPI_HOST, &t, portMAX_DELAY);
//		printf("bas: %s\n", recvbuf);


}
