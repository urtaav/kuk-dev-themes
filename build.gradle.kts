plugins {
    id("org.jetbrains.intellij.platform") version "2.9.0"
}

group = "dev.nyxdevs"
version = "1.0.0"

repositories {
    mavenCentral()
    intellijPlatform {
        defaultRepositories()
    }
}

dependencies {
    intellijPlatform {
        intellijIdeaCommunity("2025.2")
    }
}

intellijPlatform {
    // Solo temas, no hay settings propios que indexar.
    buildSearchableOptions = false

    pluginConfiguration {
        name = "Kuk Dev Themes"
        version = project.version.toString()
        vendor {
            name = "NYX Devs"
        }
        ideaVersion {
            sinceBuild = "242"
            // Sin tope: un tema no usa APIs que se rompan entre versiones.
            untilBuild = provider { null }
        }
        changeNotes = """
            <ul>
              <li>First release: Kuk, Kuk Neon, Kuk Ember and Kuk Abyss.</li>
              <li>Charcoal UI with matching editor color schemes and solid light folder icons.</li>
              <li>Accent-colored selected row with dark text and icons (Neon, Ember, Abyss).</li>
              <li>Tree indent guides hidden for a cleaner Project view.</li>
            </ul>
        """.trimIndent()
    }

    publishing {
        // Token de JetBrains Marketplace; se define fuera del repo.
        token = providers.environmentVariable("PUBLISH_TOKEN")
    }
}
