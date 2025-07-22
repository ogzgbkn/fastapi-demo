# fastapi-demo

An example API and a set of CRUD ops to sharpen my fastapi skills. Endpoints of https://github.com/ogzgbkn/unhcr_backend are copied into this project to not waste time for thinking about possible user stories and endpoints.

# Endpoints

| Endpoint Name                         | URL                                                                                                  | Description   |IsImplemented? |
| --------------                        | ----------------                                                                                     | ------------  | ------------  |
| login                                 | api/login                                                                                            |               |               |
| signup                                | api/signup                                                                                           |               |               |
| cases                                 | api/cases                                                                                            |               |               |
| case-detail                           | api/cases/\<str:id>                                                                                  |               |               |
| case-feedback-create                  | api/cases/\<str:id>/feedback                                                                         |               |               |
| case-messages                         | api/cases/\<str:id>/messages                                                                         |               |               |
| message-media-detail                  | api/messages/\<str:messageId>/message-media/\<str:mediaId>                                           |               |               |
| case-media-detail                     | api/cases/\<str:caseId>/case-media/\<str:mediaId>                                                    |               |               |
| users                                 | api/users                                                                                            |               |               |
| user-detail                           | api/users/\<str:id>                                                                                  |               |               |
| message-media-transcription-detail    | api/messages/\<str:messageId>/message-media/\<str:mediaId>/transcription/\<str:transcriptionId>      |               |               |
| case-media-transcription-detail       | api/cases/\<str:caseId>/case-media/\<str:mediaId>/transcription/\<str:transcriptionId>               |               |               |
| user-devices                          | api/user-devices                                                                                     |               |               |
| user-device-detail                    | api/user-devices/\<str:id>                                                                           |               |               |