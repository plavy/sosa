package hr.fer.lab1.security;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.oauth2.server.resource.OAuth2ResourceServerConfigurer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.web.SecurityFilterChain;

@EnableWebSecurity
@Configuration
public class WebSecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests()
                .antMatchers("/").permitAll()
                .antMatchers("/students").hasAnyRole("USER", "ADMIN")
                .antMatchers("/resources").hasAnyRole("ADMIN")
                .anyRequest().authenticated();
//        http.oauth2ResourceServer(oauth2 -> oauth2
//                .jwt(jwt -> jwt
//                        .jwtAuthenticationConverter(new CustomAuthenticationConverter())
//                )
//        );
        http.oauth2ResourceServer(OAuth2ResourceServerConfigurer::jwt);
        http.oauth2Login();

        return http.build();
    }

//    static class CustomAuthenticationConverter implements Converter<Jwt, AbstractAuthenticationToken> {
//        public AbstractAuthenticationToken convert(Jwt jwt) {
//        }
//    }

}
