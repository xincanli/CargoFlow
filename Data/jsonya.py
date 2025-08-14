import json
import yaml

# 假设这是你的 JSON-LD 数据，字符串格式
json_ld_str = '''
      
      
{
      "@context": {
        "cargo": "https://onerecord.iata.org/ns/cargo#",
        "code": "https://onerecord.iata.org/ns/code-lists/"
    },
     "@type": "cargo:Waybill",
    "cargo:waybillType": {
        "@id": "cargo:MASTER"
    },
    "cargo:involvedParties": [
        {
            "@type": "cargo:Party",
            "cargo:partyDetails": {
                "@type": "cargo:Organization",
                "cargo:name": "OCS SHANGHAI CO LTD",
                "cargo:basedAtLocation": {
                    "@type": "cargo:Location",
                   "cargo:locationName": "KEYUANWEI3ROAD 21"
                }
            },
            "cargo:partyRole": {
                "@type": "code:ParticipantIdentifier",
                "@id": "https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#SHP"
            }
        },
        {
            "@type": "cargo:Party",
            "cargo:partyDetails": {
                "@type": "cargo:Organization",
                "cargo:name": "OCS OSAKA OFFICE",
                "cargo:basedAtLocation": {
                    "@type": "cargo:Location",
                  "cargo:locationName": "1SENSHU KUKO MINAMI SENNAN"
                }
            },
            "cargo:partyRole": {
                "@type": "code:ParticipantIdentifier",
                "@id": "https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#CNE"
            }
        }
    ],
    "cargo:accountingInformation":"运单修改1次 08700002",
    "cargo:departureLocation": {
        "@type": "cargo:Location",
        "cargo:locationCodes": {
            "@type": "cargo:CodeListElement",
            "cargo:code": "TAO"
        },
        "cargo:locationName":"QINGDAO"
    },
    "cargo:arrivalLocation": {
        "@type": "cargo:Location",
        "cargo:locationCodes": {
            "@type": "cargo:CodeListElement",
            "cargo:code": "KIX"
        },
        "cargo:locationName":"OSAKA"
    },
    "cargo:referredBookingOption":{
    "@type":"cargo:Booking",
    "cargo:activitySequences":[
      { 
        "@type":"cargo:ActivitySequence",
        "cargo:activity":{
            "@type":"cargo:Transportmovement",
            "@cargo:transportIdentifier":{
                "@type":"http://www.w3.org/2001/XMLSchema#string",
                "@value":"SC2433/18JUL"
            }
        }
      }
    ]
    },
        "cargo:waybillLineItems": [
        {
            "@type": "cargo:WaybillLineItem",
            "@cargo:lineItemPackages":[
                {
                    "type":"cargo:LineItemPackage",
                    "cargo:pieceReferences":[
                        {
                             "@type":"cargo:Piece",
                             "cargo:involvedInActions":{
                                 "@type":"cargo:Loading",
                                 "cargo:servedActivity":{
                                     "@type":"cargo:TransportMovement",
                                     "cargo:transportIdentifier":{
                                          "@type": "http://www.w3.org/2001/XMLSchema#string",
                                          "@value": "SC2433/18JUL"
                                     },
                                     "cargo:movementTimes":[
                                         {
                                             "@type":"cargo:MovementTime",
                                             "cargo:movementTimestamp":{
                                                 "@type": "http://www.w3.org/2001/XMLSchema#dateTime",
                                                 "@value": "2025/7/18"
                                             }
                                         }
                                     ]
                                 }
                             },
                             "cargo:volumetricWeight":{
                                 "@type":"cargo:VolumetricWeight",
                                 "cargo:chargeableWeight":{
                                     "@type":"cargo:Value",
                                     "cargo:numericalValue":{
                                         "@type":"cargo:http://www.w3.org/2001/XMLSchema#double",
                                         "@value":1500
                                     },
                                     "cargo:unit":{
                                         "@id":"https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#KGM"
                                     }
                                 }
                             }
                         }
                     ]
                }
            ],
            "cargo:rateClassCode": {
                "@id": "https://onerecord.iata.org/ns/code-lists/RateClassCode#Q"
            },
            "cargo:rateCharge": {
                "@type": "cargo:CurrencyValue",
                "cargo:currencyUnit": {
                    "@type": "code:CurrencyCode",
                    "@value": "https://vocabulary.uncefact.org/CurrencyCodeList#CNY"
                },
                "cargo:numericalValue": 0
            },
            "cargo:rateVolume":{
                "@type": "cargo:CurrencyValue",
                "cargo:currencyUnit": {
                    "@type": "code:CurrencyCode",
                    "@value": "https://vocabulary.uncefact.org/CurrencyCodeList#CNY"
                },
                "cargo:numericalValue": 9
            }
        }
    ],
       "cargo:weightValuationIndicator": {
        "@type": "code:PrepaidCollectIndicator",
        "@id": "https://onerecord.iata.org/ns/code-lists/PrepaidCollectIndicator#P"
    },
    "cargo:otherChargesIndicator": {
        "@type": "code:PrepaidCollectIndicator",
        "@id": "code:PrepaidCollectIndicator#P"
    },
    "cargo:declaredValueForCarriage": {
        "@type": "cargo:CurrencyValue",
        "cargo:currencyUnit": {
            "@type": "code:CurrencyCode",
            "@id": "https://vocabulary.uncefact.org/CurrencyCodeList#CNY"
        },
        "cargo:numericalValue": {
            "@type":"http://www.w3.org/2001/XMLSchema#double",
            "@value":0
        }
    },
      "cargo:declaredValueForCustoms": {
        "@type": "cargo:CurrencyValue",
        "cargo:currencyUnit": {
            "@type": "code:CurrencyCode",
            "@value": "https://vocabulary.uncefact.org/CurrencyCodeList#CNY"
        },
        "cargo:numericalValue": {
            "@type":"http://www.w3.org/2001/XMLSchema#double",
            "@value":0
        }
    },
     "cargo:shipment": {
        "@type": "cargo:Shipment",
        "cargo:insurance": {
            "@type": "cargo:Insurance",
            "cargo:insuredAmount": {
                "@type": "cargo:CurrencyValue",
                "cargo:currencyUnit": {
                    "@type": "code:CurrencyCode",
                    "@id": "https://vocabulary.uncefact.org/CurrencyCodeList#USD"
                },
                "cargo:numericalValue": 0
            }
        },
        "cargo:totalGrossWeight": {
            "@type": "cargo:Value",
            "cargo:numericalValue":927,
            "cargo:unit":{
                "@id": "https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#KGM"
            }
        },
        "cargo:goodsDescription":"EXPRESS"
     },
    "cargo:carrierDeclarationDate": {
        "@type": "http://www.w3.org/2001/XMLSchema#dateTime",
        "@value": "2025/7/17"
    },
    "cargo:carrierDeclarationPlace": {
        "@type": "cargo:Location",
        "cargo:locationCodes": [
            {
            "@type": "cargo:CodeListElement",
            "cargo:code": "TNA"
        }
    ]
    }
}

'''

# 第一步：用 json.loads() 把 JSON-LD 字符串转换成 Python 字典
data_dict = json.loads(json_ld_str)

# 第二步：用 pyyaml 的 yaml.dump() 把字典转换成 YAML 格式字符串
yaml_str = yaml.dump(data_dict, allow_unicode=True, default_flow_style=False)

# 输出结果看看
print(yaml_str)
