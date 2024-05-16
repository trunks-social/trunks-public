# Trunks project management, issue tracker, and translation hub.

Click the issues tab above and help report issues that you're seeing across any of the platforms.

## Translating

Translation is managed in crowdin, see https://crowdin.com/project/trunkssocial for contributions.

### Manual translation

Checkout the `app_en.arb` file to see the current english translation for the application.

To translate into a new language, create a new arb file specific to that language locale.

For the hello world translation example, you can see the original source as the following:

`app_en.arb`
```json
{
  "helloWorld": "Hello World!",
  "@helloWorld": {
    "description": "The conventional newborn programmer greeting"
  }
}
```

For the spanish translation, you would then have an `es` version that contained the translated text.
`app_es.arb`
```json
{
    "helloWorld": "¡Hola Mundo!"
}
```

Please reference: https://docs.flutter.dev/ui/accessibility-and-localization/internationalization

Note, the files here will be synchronized often but the binaries will still need to updated for each application store.
