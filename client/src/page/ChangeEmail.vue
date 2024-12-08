<template>

</template>

<style></style>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            Error: 404,
        }

    },
    mounted() {
        if (this.$route.query.token) {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `auth/change-email`),
                withCredentials: true,
                data: {
                    token: this.$route.query.token,
                    new_email: this.$route.query.new_email
                },
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    this.$router.push({
                        name: 'homeview',
                    })
                    localStorage.showver = 1
                })
                .catch(error => {
                    if (error.status != null) {
                        this.$router.push({
                            name: 'codeerrorview',
                            query: {
                                ErrorNum: error.status
                            }
                        })
                    }
                });
        }
        else {
            this.$router.push({
                name: 'codeerrorview',
                query: {
                    ErrorNum: 404
                }
            })
        }
    },
}

</script>
